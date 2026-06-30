import json
from pathlib import Path

from parsers.csv_parser import CSVParser
from parsers.txt_parser import TXTParser

from services.validator import Validator
from services.normalizer import Normalizer
from services.deduplicator import Deduplicator
from services.conflict_resolver import ConflictResolver
from services.confidence_engine import ConfidenceEngine
from services.projection_engine import ProjectionEngine

from utils.logger import logger


INPUT_FOLDER = Path("input")
OUTPUT_FOLDER = Path("output")
CONFIG = "config/output_config.json"


def process_candidates():

    logger.info("Starting Candidate Transformation...")

    csv_parser = CSVParser()
    txt_parser = TXTParser()

    candidates = []

    # ----------------------------
    # Parse CSV
    # ----------------------------

    csv_file = INPUT_FOLDER / "recruiter.csv"

    if csv_file.exists():

        logger.info("Parsing Recruiter CSV...")

        candidates.extend(
            csv_parser.parse(csv_file)
        )

    # ----------------------------
    # Parse TXT
    # ----------------------------

    txt_file = INPUT_FOLDER / "recruiter_notes.txt"

    if txt_file.exists():

        logger.info("Parsing Recruiter Notes...")

        candidates.extend(
            txt_parser.parse(txt_file)
        )

    logger.info(f"Candidates Parsed : {len(candidates)}")

    # ----------------------------
    # Validation
    # ----------------------------

    logger.info("Validating Candidates...")

    candidates = [

        Validator.validate(candidate)

        for candidate in candidates

    ]

    # ----------------------------
    # Normalization
    # ----------------------------

    logger.info("Normalizing Candidate Data...")

    candidates = [

        Normalizer.normalize(candidate)

        for candidate in candidates

    ]

    # ----------------------------
    # Merge
    # ----------------------------

    logger.info("Deduplicating Candidates...")

    candidates = Deduplicator.merge(candidates)

    logger.info(f"Unique Candidates : {len(candidates)}")

    # ----------------------------
    # Resolve
    # ----------------------------

    logger.info("Resolving Conflicts...")

    candidates = [

        ConflictResolver.resolve(candidate)

        for candidate in candidates

    ]

    # ----------------------------
    # Confidence
    # ----------------------------

    logger.info("Calculating Confidence...")

    candidates = [

        ConfidenceEngine.calculate(candidate)

        for candidate in candidates

    ]

    # ----------------------------
    # Projection
    # ----------------------------

    logger.info("Generating Final Output...")

    result = [

        ProjectionEngine.project(
            candidate,
            CONFIG
        )

        for candidate in candidates

    ]

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    output_file = OUTPUT_FOLDER / "candidate_output.json"

    with open(output_file, "w") as f:

        json.dump(

            result,

            f,

            indent=4,

            default=str

        )

    logger.success("Transformation Completed")

    logger.success(f"Output saved to {output_file}")


if __name__ == "__main__":

    process_candidates()