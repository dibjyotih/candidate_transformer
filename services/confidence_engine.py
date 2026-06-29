from models.candidate import Candidate

from models.confidence import Confidence


class ConfidenceEngine:

    @staticmethod
    def calculate(candidate: Candidate):

        total = 0.5

        if candidate.emails:

            candidate.confidence.append(
                Confidence(field="emails", score=0.9)
            )

            total += 0.15

        if candidate.phones:

            candidate.confidence.append(
                Confidence(field="phones", score=0.9)
            )

            total += 0.15

        if candidate.skills:

            candidate.confidence.append(
                Confidence(field="skills", score=0.8)
            )

            total += 0.1

        if candidate.experience:

            candidate.confidence.append(
                Confidence(field="experience", score=0.8)
            )

            total += 0.1

        candidate.overall_confidence = min(total, 1.0)

        return candidate