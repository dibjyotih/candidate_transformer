from models.candidate import Candidate


class ConflictResolver:
    """
    Resolves conflicting candidate information after deduplication.
    """

    SOURCE_PRIORITY = {
        "Recruiter Notes": 2,
        "Recruiter CSV": 1
    }

    @staticmethod
    def resolve(candidate: Candidate) -> Candidate:

        # -----------------------------
        # Resolve Name
        # -----------------------------

        if candidate.personal.full_name:

            candidate.personal.full_name = (
                candidate.personal.full_name.strip()
            )

        # -----------------------------
        # Resolve Headline
        # -----------------------------

        if candidate.professional.headline:

            candidate.professional.headline = (
                candidate.professional.headline.strip()
            )

        # -----------------------------
        # Resolve Experience
        # Keep highest years
        # -----------------------------

        if candidate.professional.years_experience:

            candidate.professional.years_experience = max(
                0,
                candidate.professional.years_experience
            )

        # -----------------------------
        # Remove duplicate companies
        # -----------------------------

        unique_companies = {}

        for exp in candidate.professional.experience:

            if exp.company:

                key = exp.company.lower()

                if key not in unique_companies:

                    unique_companies[key] = exp

        candidate.professional.experience = list(
            unique_companies.values()
        )

        # -----------------------------
        # Remove duplicate education
        # -----------------------------

        unique_education = {}

        for edu in candidate.education:

            key = (
                str(edu.degree),
                str(edu.institution)
            )

            if key not in unique_education:

                unique_education[key] = edu

        candidate.education = list(
            unique_education.values()
        )

        # -----------------------------
        # Remove duplicate skills
        # -----------------------------

        candidate.professional.skills = sorted(
            list(
                set(candidate.professional.skills)
            )
        )

        # -----------------------------
        # Remove duplicate links
        # -----------------------------

        candidate.links = sorted(
            list(
                set(candidate.links)
            )
        )

        # -----------------------------
        # Remove duplicate emails
        # -----------------------------

        candidate.personal.emails = sorted(
            list(
                set(candidate.personal.emails)
            )
        )

        # -----------------------------
        # Remove duplicate phones
        # -----------------------------

        candidate.personal.phones = sorted(
            list(
                set(candidate.personal.phones)
            )
        )

        return candidate