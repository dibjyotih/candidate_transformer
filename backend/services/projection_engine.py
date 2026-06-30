import json

from models.candidate import Candidate


class ProjectionEngine:

    @staticmethod
    def project(candidate: Candidate, config_path: str):

        with open(config_path) as f:
            config = json.load(f)

        result = {}

        for field in config["fields"]:

            source = field["from"]
            target = field["path"]

            value = ProjectionEngine.resolve_path(
                candidate,
                source
            )

            result[target] = value

        if config.get("include_confidence", True):

            result["confidence"] = (
                candidate.metadata.confidence
            )

        if config.get("include_provenance", True):

            result["provenance"] = (
                candidate.provenance
            )

        return result

    @staticmethod
    def resolve_path(obj, path):

        current = obj

        for part in path.split("."):

            if current is None:
                return None

            if isinstance(current, dict):
                current = current.get(part)

            else:
                current = getattr(current, part, None)

        return current