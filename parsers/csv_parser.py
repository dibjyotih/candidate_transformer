import uuid
import pandas as pd

from models.candidate import Candidate
from parsers.base_parser import BaseParser
from models.provenance import Provenance

class CSVParser(BaseParser):
    def parse(self,path:str):
        df= pd.read_csv(path)
        candidates= []

        for _, row in df.iterrows():
            candidate= Candidate(
                candidate_id= str(uuid.uuid4()),
                full_name= row.get("full_name"),
                emails= [row.get("emails")] if pd.notna(row.get("emails")) else [],
                phones= [str(row.get("phone"))] if pd.notna(row.get("phone")) else [],
                headline= row.get("title")
            )
            candidate.provenance.extend([

                Provenance(field="full_name",
                           source="csv",
                           method="parsed"),

                Provenance(field="emails",
                           source="csv",
                           method="parsed"),

                Provenance(field="phones",
                           source="csv",
                           method="parsed"),

                Provenance(field="headline",
                           source="csv",
                           method="parsed")

            ])
            candidates.append(candidate)

        return candidates