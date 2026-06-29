import re
import uuid

from models.candidate import Candidate
from models.provenance import Provenance
from parsers.base_parser import BaseParser


class TXTParser(BaseParser):

    EMAIL = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    PHONE = r"(\+?\d[\d\s-]{8,}\d)"

    SKILLS = [
        "Python",
        "Java",
        "SQL",
        "C++",
        "Machine Learning",
        "React",
        "AWS",
        "Docker"
    ]

    def parse(self, path):

        text = open(path,
                    encoding="utf8").read()

        emails = re.findall(self.EMAIL,
                            text)

        phones = re.findall(self.PHONE,
                            text)

        skills = []

        for skill in self.SKILLS:

            if skill.lower() in text.lower():

                skills.append(skill)

        first_line = text.split("\n")[0]

        candidate = Candidate(

            candidate_id=str(uuid.uuid4()),

            full_name=first_line,

            emails=emails,

            phones=phones,

            skills=skills

        )

        candidate.provenance.extend([

            Provenance(field="full_name",
                       source="txt",
                       method="regex"),

            Provenance(field="emails",
                       source="txt",
                       method="regex"),

            Provenance(field="phones",
                       source="txt",
                       method="regex"),

            Provenance(field="skills",
                       source="txt",
                       method="keyword")

        ])

        return [candidate]