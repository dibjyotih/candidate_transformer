from pathlib import Path
from typing import List
import uuid
import re

from parsers.base_parser import BaseParser

from models.candidate import (
    Candidate,
    Experience,
    Education
)

from utils.constants import (
    EMAIL_REGEX,
    PHONE_REGEX,
    KNOWN_SKILLS,
    KNOWN_DEGREES
)


class TXTParser(BaseParser):

    def supports(self, file_path: Path) -> bool:
        return file_path.suffix.lower() == ".txt"

    def parse(self, file_path: Path) -> List[Candidate]:

        text = file_path.read_text(encoding="utf-8")

        # Split multiple candidates
        sections = re.split(
            r"\n[-=]{5,}\n",
            text
        )

        candidates = []

        for section in sections:

            section = section.strip()

            if len(section) < 10:
                continue

            candidate = Candidate(
                candidate_id=str(uuid.uuid4())
            )

            lower = section.lower()

            lines = [
                line.strip()
                for line in section.splitlines()
                if line.strip()
            ]

            # --------------------------------------------------
            # NAME
            # --------------------------------------------------

            name = None

            for line in lines:

                if line.lower().startswith("candidate name"):

                    name = line.split(":", 1)[1].strip()
                    break

            if name is None and len(lines) > 0:

                if not lines[0].startswith("="):
                    name = lines[0]

            candidate.personal.full_name = name

            # --------------------------------------------------
            # EMAIL
            # --------------------------------------------------

            candidate.personal.emails.extend(
                EMAIL_REGEX.findall(section)
            )

            # --------------------------------------------------
            # PHONE
            # --------------------------------------------------

            candidate.personal.phones.extend(
                PHONE_REGEX.findall(section)
            )

            # --------------------------------------------------
            # EXPERIENCE YEARS
            # --------------------------------------------------

            match = re.search(
                r"experience\s*:?\s*(\d+)",
                section,
                re.IGNORECASE
            )

            if match:

                candidate.professional.years_experience = float(
                    match.group(1)
                )

            # --------------------------------------------------
            # HEADLINE
            # --------------------------------------------------

            professions = [

                "engineer",
                "developer",
                "scientist",
                "architect",
                "manager",
                "consultant",
                "analyst"

            ]

            for line in lines:

                if any(
                    profession in line.lower()
                    for profession in professions
                ):

                    candidate.professional.headline = line
                    break

            # --------------------------------------------------
            # SKILLS
            # --------------------------------------------------

            skills = []

            for skill in KNOWN_SKILLS:

                if skill.lower() in lower:

                    skills.append(skill)

            candidate.professional.skills = sorted(
                list(set(skills))
            )

            # --------------------------------------------------
            # COMPANIES
            # --------------------------------------------------

            companies = re.findall(
                r"worked at\s+([A-Za-z0-9 &]+)",
                section,
                re.IGNORECASE
            )

            for company in companies:

                candidate.professional.experience.append(

                    Experience(

                        company=company.strip(),

                        title=candidate.professional.headline

                    )

                )

            # --------------------------------------------------
            # EDUCATION
            # --------------------------------------------------

            for degree in KNOWN_DEGREES:

                if degree.lower() in lower:

                    candidate.education.append(

                        Education(

                            degree=degree

                        )

                    )

            # --------------------------------------------------
            # LINKS
            # --------------------------------------------------

            urls = re.findall(
                r"https?://\S+",
                section
            )

            candidate.links.extend(urls)

            # --------------------------------------------------
            # SOURCE
            # --------------------------------------------------

            candidate.metadata.sources.append(
                "Recruiter Notes"
            )

            # --------------------------------------------------
            # PROVENANCE
            # --------------------------------------------------

            if candidate.personal.full_name:

                candidate.provenance.append({

                    "field": "personal.full_name",

                    "value": candidate.personal.full_name,

                    "source": "Recruiter Notes",

                    "method": "Section Parsing"

                })

            for email in candidate.personal.emails:

                candidate.provenance.append({

                    "field": "personal.emails",

                    "value": email,

                    "source": "Recruiter Notes",

                    "method": "Regex"

                })

            for phone in candidate.personal.phones:

                candidate.provenance.append({

                    "field": "personal.phones",

                    "value": phone,

                    "source": "Recruiter Notes",

                    "method": "Regex"

                })

            if candidate.professional.headline:

                candidate.provenance.append({

                    "field": "professional.headline",

                    "value": candidate.professional.headline,

                    "source": "Recruiter Notes",

                    "method": "Keyword"

                })

            for skill in candidate.professional.skills:

                candidate.provenance.append({

                    "field": "professional.skills",

                    "value": skill,

                    "source": "Recruiter Notes",

                    "method": "Keyword Matching"

                })

            for exp in candidate.professional.experience:

                candidate.provenance.append({

                    "field": "professional.experience",

                    "value": exp.company,

                    "source": "Recruiter Notes",

                    "method": "Regex"

                })

            for edu in candidate.education:

                candidate.provenance.append({

                    "field": "education",

                    "value": edu.degree,

                    "source": "Recruiter Notes",

                    "method": "Keyword Matching"

                })

            candidates.append(candidate)

        return candidates