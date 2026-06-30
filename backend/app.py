import json
import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from parsers.csv_parser import CSVParser
from parsers.txt_parser import TXTParser

from services.validator import Validator
from services.normalizer import Normalizer
from services.deduplicator import Deduplicator
from services.conflict_resolver import ConflictResolver
from services.confidence_engine import ConfidenceEngine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

INPUT_FOLDER = Path("input")
CONFIG = "config/output_config.json"

INPUT_FOLDER.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {"message": "Candidate Transformer Running"}


@app.post("/transform")
async def transform(
    csv: UploadFile = File(...),
    notes: UploadFile = File(...)
):

    csv_path = INPUT_FOLDER / "recruiter.csv"
    txt_path = INPUT_FOLDER / "recruiter_notes.txt"

    with open(csv_path, "wb") as buffer:
        shutil.copyfileobj(csv.file, buffer)

    with open(txt_path, "wb") as buffer:
        shutil.copyfileobj(notes.file, buffer)

    csv_parser = CSVParser()
    txt_parser = TXTParser()

    candidates = []

    candidates.extend(csv_parser.parse(csv_path))
    candidates.extend(txt_parser.parse(txt_path))

    candidates = [
        Validator.validate(c)
        for c in candidates
    ]

    candidates = [
        Normalizer.normalize(c)
        for c in candidates
    ]

    candidates = Deduplicator.merge(candidates)

    candidates = [
        ConflictResolver.resolve(c)
        for c in candidates
    ]

    candidates = [
        ConfidenceEngine.calculate(c)
        for c in candidates
    ]

    result = [
        c.model_dump()
        for c in candidates
    ]

    return result