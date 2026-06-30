import re

from models.candidate import Candidate


class Normalizer:

    SKILL_MAPPING = {

        "py": "Python",
        "python3": "Python",
        "python": "Python",

        "cpp": "C++",
        "c++": "C++",

        "js": "JavaScript",
        "javascript": "JavaScript",

        "ts": "TypeScript",
        "typescript": "TypeScript",

        "ml": "Machine Learning",
        "machine learning": "Machine Learning",

        "postgres": "PostgreSQL",
        "postgresql": "PostgreSQL",

        "node": "Node.js",
        "nodejs": "Node.js",
        "node.js": "Node.js",

        "reactjs": "React",
        "react.js": "React"
    }

    COMPANY_MAPPING = {

        "google llc": "Google",
        "google india": "Google",

        "amazon web services": "Amazon",
        "aws": "Amazon",

        "microsoft corporation": "Microsoft"
    }

    DEGREE_MAPPING = {

        "btech": "B.Tech",
        "b.tech": "B.Tech",

        "mtech": "M.Tech",
        "m.tech": "M.Tech",

        "be": "B.E",
        "b.e": "B.E"
    }
    

    @staticmethod
    def normalize(candidate: Candidate):

        # ---------------------------------
        # Name
        # ---------------------------------

        if candidate.personal.full_name:

            candidate.personal.full_name = " ".join(

                word.capitalize()

                for word in

                candidate.personal.full_name.strip().split()

            )

        # ---------------------------------
        # Emails
        # ---------------------------------

        candidate.personal.emails = [

            email.lower().strip()

            for email in candidate.personal.emails

        ]

        # ---------------------------------
        # Location
        # ---------------------------------

        if candidate.personal.location:

            candidate.personal.location = candidate.personal.location.title()

        # ---------------------------------
        # Skills
        # ---------------------------------

        normalized_skills = []

        for skill in candidate.professional.skills:

            key = skill.lower().strip()

            normalized_skills.append(

                Normalizer.SKILL_MAPPING.get(

                    key,

                    skill.title()

                )

            )

        candidate.professional.skills = sorted(

            list(

                set(normalized_skills)

            )

        )

        # ---------------------------------
        # Company Names
        # ---------------------------------

        for exp in candidate.professional.experience:

            if exp.company:

                company = exp.company.lower().strip()

                exp.company = Normalizer.COMPANY_MAPPING.get(

                    company,

                    exp.company.title()

                )

        # ---------------------------------
        # Degree Names
        # ---------------------------------

        for edu in candidate.education:

            if edu.degree:

                degree = edu.degree.lower().strip()

                edu.degree = Normalizer.DEGREE_MAPPING.get(

                    degree,

                    edu.degree

                )

        # ---------------------------------
        # Remove Duplicate Emails
        # ---------------------------------

        candidate.personal.emails = sorted(

            list(

                set(candidate.personal.emails)

            )

        )

        # ---------------------------------
        # Remove Duplicate Phones
        # ---------------------------------

        candidate.personal.phones = sorted(

            list(

                set(candidate.personal.phones)

            )

        )

        # ---------------------------------
        # Remove Duplicate Links
        # ---------------------------------

        candidate.links = sorted(

            list(

                set(candidate.links)

            )

        )

        return candidate