import phonenumbers

from dateutil import parser

from models.candidate import Candidate


class Normalizer:

    SKILL_MAP = {

        "cpp": "C++",
        "c++": "C++",

        "py": "Python",

        "python3": "Python",

        "machine learning": "Machine Learning",

        "ml": "Machine Learning"

    }

    @staticmethod
    def normalize(candidate: Candidate):

        candidate.emails = [
            email.lower().strip()
            for email in candidate.emails
        ]

        phones = []

        for phone in candidate.phones:

            try:

                number = phonenumbers.parse(phone, "IN")

                phones.append(
                    phonenumbers.format_number(
                        number,
                        phonenumbers.PhoneNumberFormat.E164
                    )
                )

            except:
                phones.append(phone)

        candidate.phones = phones

        normalized = []

        for skill in candidate.skills:

            key = skill.lower().strip()

            normalized.append(
                Normalizer.SKILL_MAP.get(key, skill.title())
            )

        candidate.skills = sorted(list(set(normalized)))

        for exp in candidate.experience:

            if exp.start:
                try:
                    exp.start = parser.parse(exp.start).strftime("%Y-%m")
                except:
                    pass

            if exp.end:
                try:
                    exp.end = parser.parse(exp.end).strftime("%Y-%m")
                except:
                    pass

        return candidate