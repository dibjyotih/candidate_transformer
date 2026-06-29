from typing import List, Optional
from pydantic import BaseModel

from models.provenance import Provenance
from models.confidence import Confidence

class Experience(BaseModel):
    company: Optional[str]= None
    title: Optional[str]= None
    start: Optional[str]= None
    end: Optional[str]= None
    summary: Optional[str]= None

class Education(BaseModel):
    institution: Optional[str]= None
    degree: Optional[str]= None
    field: Optional[str]= None
    end_year: Optional[str]= None

class Candidate(BaseModel):
    candidate_id: Optional[str] = None
    full_name: Optional[str] = None
    emails: List[str] = []
    phones: List[str] = []
    location: Optional[str] = None
    headline: Optional[str] = None
    years_experience: Optional[float] = None
    skills: List[str] = []
    experience: List[Experience] = []
    education: List[Education] = []
    links: List[str] = []
    provenance: List[Provenance] = []
    confidence: List[Confidence] = []
    overall_confidence: float = 0.0