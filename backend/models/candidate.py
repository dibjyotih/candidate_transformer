from typing import List, Optional
from pydantic import BaseModel, Field


class Experience(BaseModel):
    company: Optional[str] = None
    title: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None


class Education(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None


class PersonalInfo(BaseModel):
    full_name: Optional[str] = None
    emails: List[str] = Field(default_factory=list)
    phones: List[str] = Field(default_factory=list)
    location: Optional[str] = None


class ProfessionalInfo(BaseModel):
    headline: Optional[str] = None
    years_experience: Optional[float] = None
    skills: List[str] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)


class CandidateMetadata(BaseModel):
    sources: List[str] = Field(default_factory=list)
    confidence: float = 0.0


class Candidate(BaseModel):
    candidate_id: str

    personal: PersonalInfo = Field(default_factory=PersonalInfo)

    professional: ProfessionalInfo = Field(default_factory=ProfessionalInfo)

    education: List[Education] = Field(default_factory=list)

    links: List[str] = Field(default_factory=list)

    provenance: List[dict] = Field(default_factory=list)

    metadata: CandidateMetadata = Field(default_factory=CandidateMetadata)