from pathlib import Path
from typing import List
import uuid

import pandas as pd

from models.candidate import (
    Candidate,
    PersonalInfo,
    ProfessionalInfo,
    Experience
)

from parsers.base_parser import BaseParser


class CSVParser(BaseParser):

    COLUMN_MAP = {
        "name": [
            "name",
            "candidate_name",
            "full_name"
        ],

        "email": [
            "email",
            "email_address",
            "mail"
        ],

        "phone": [
            "phone",
            "mobile",
            "mobile_number",
            "contact"
        ],

        "headline": [
            "title",
            "designation",
            "headline"
        ],

        "company": [
            "current_company",
            "company",
            "organization"
        ],

        "location": [
            "location",
            "city"
        ],

        "experience": [
            "years_experience",
            "experience"
        ],

        "skills": [
            "skills",
            "tech_stack"
        ]
    }

    def supports(self, file_path: Path):

        return file_path.suffix.lower() == ".csv"

    def _find_column(self, columns, aliases):

        for alias in aliases:

            if alias in columns:

                return alias

        return None

    def parse(self, file_path: Path) -> List[Candidate]:

        df = pd.read_csv(file_path)

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

        candidates = []

        for _, row in df.iterrows():

            candidate = Candidate(
                candidate_id=str(uuid.uuid4())
            )

            columns = df.columns

            # -----------------------
            # Personal Information
            # -----------------------

            name_col = self._find_column(
                columns,
                self.COLUMN_MAP["name"]
            )

            if name_col:

                candidate.personal.full_name = row[name_col]

            email_col = self._find_column(
                columns,
                self.COLUMN_MAP["email"]
            )

            if email_col and pd.notna(row[email_col]):

                candidate.personal.emails.append(
                    str(row[email_col])
                )

            phone_col = self._find_column(
                columns,
                self.COLUMN_MAP["phone"]
            )

            if phone_col and pd.notna(row[phone_col]):

                candidate.personal.phones.append(
                    str(row[phone_col])
                )

            location_col = self._find_column(
                columns,
                self.COLUMN_MAP["location"]
            )

            if location_col:

                candidate.personal.location = row[location_col]

            # -----------------------
            # Professional
            # -----------------------

            headline_col = self._find_column(
                columns,
                self.COLUMN_MAP["headline"]
            )

            if headline_col:

                candidate.professional.headline = row[headline_col]

            exp_col = self._find_column(
                columns,
                self.COLUMN_MAP["experience"]
            )

            if exp_col:

                try:

                    candidate.professional.years_experience = float(
                        row[exp_col]
                    )

                except:

                    pass

            company_col = self._find_column(
                columns,
                self.COLUMN_MAP["company"]
            )

            company = row.get(company_col)

            if pd.notna(company):

                candidate.professional.experience.append(

                    Experience(

                        company=str(company),

                        title=candidate.professional.headline

                    )
            )

            skills_col = self._find_column(
                columns,
                self.COLUMN_MAP["skills"]
            )

            if skills_col and pd.notna(row[skills_col]):

                skills = str(row[skills_col])

                candidate.professional.skills = [

                    skill.strip()

                    for skill in skills.replace(",", "|").split("|")

                    if skill.strip()

                ]

            # -----------------------
            # Metadata
            # -----------------------

            candidate.metadata.sources.append("Recruiter CSV")

            candidate.provenance.extend([

                {

                    "field": "personal",

                    "source": "Recruiter CSV"

                },

                {

                    "field": "professional",

                    "source": "Recruiter CSV"

                }

            ])

            candidates.append(candidate)

        return candidates