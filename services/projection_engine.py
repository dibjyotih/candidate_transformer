import json


class ProjectionEngine:

    @staticmethod
    def project(candidate, config_path):

        with open(config_path) as f:
            config = json.load(f)

        output = {}

        include_confidence = config.get("include_confidence", True)

        for field in config["fields"]:

            source = field["from"]

            target = field["path"]

            output[target] = getattr(candidate, source, None)

        if include_confidence:

            output["overall_confidence"] = candidate.overall_confidence

            output["confidence"] = [
                c.model_dump()
                for c in candidate.confidence
            ]

        output["provenance"] = [
            p.model_dump()
            for p in candidate.provenance
        ]

        return output