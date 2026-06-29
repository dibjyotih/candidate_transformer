from pydantic import BaseModel

class Confidence(BaseModel):
    field: str
    score: float