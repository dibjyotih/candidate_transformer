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


INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
CONFIG = "config/output_config.json"


def main():

    csv_parser = CSVParser()
    txt_parser = TXTParser()

    candidates = []

    # Parse CSV
    candidates.extend(
        csv_parser.parse(INPUT_DIR / "recruiter.csv")
    )

    # Parse Notes
    candidates.extend(
        txt_parser.parse(INPUT_DIR / "recruiter_notes.txt")
    )

    # Validation
    validated = [
        Validator.validate(c)
        for c in candidates
    ]

    # Normalization
    normalized = [
        Normalizer.normalize(c)
        for c in validated
    ]

    # Deduplicate
    merged = Deduplicator.merge(normalized)

    final_output = []

    for candidate in merged:

        candidate = ConflictResolver.resolve(candidate)

        candidate = ConfidenceEngine.calculate(candidate)

        result = ProjectionEngine.project(
            candidate,
            CONFIG
        )

        final_output.append(result)

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_DIR / "candidate_output.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("Transformation Complete.")


if __name__ == "__main__":
    main()