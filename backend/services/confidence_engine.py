from models.candidate import Candidate


class ConfidenceEngine:

    @staticmethod
    def calculate(candidate: Candidate) -> Candidate:

        score = 0.0

        # Personal Information
        if candidate.personal.full_name:
            score += 0.10

        if candidate.personal.emails:
            score += 0.15

        if candidate.personal.phones:
            score += 0.15

        if candidate.personal.location:
            score += 0.10

        # Professional Information
        if candidate.professional.headline:
            score += 0.10

        if candidate.professional.skills:
            score += 0.15

        if candidate.professional.experience:
            score += 0.10

        if candidate.professional.years_experience:
            score += 0.10

        # Education
        if candidate.education:
            score += 0.05

        candidate.metadata.confidence = round(
            min(score, 1.0),
            2
        )

        return candidate