# Multi-Source Candidate Data Transformer

Engineering Assignment for the Eightfold AI Engineering Intern (Jul-Dec 2026)

## Overview

This project transforms candidate information from multiple sources into a single canonical candidate profile. It supports both structured and unstructured inputs, resolves duplicate records, tracks data provenance, and assigns a confidence score to each candidate.

### Supported Sources

- Recruiter CSV (Structured)
- Recruiter Notes TXT (Unstructured)

---

## Features

- Parse CSV and TXT files
- Normalize candidate information
- Merge duplicate candidates
- Resolve conflicting values
- Generate confidence scores
- Track field-level provenance
- React-based UI
- FastAPI REST API

---

## Pipeline

```
CSV + TXT
    │
    ▼
Parsing
    ▼
Validation
    ▼
Normalization
    ▼
Deduplication
    ▼
Conflict Resolution
    ▼
Confidence Calculation
    ▼
Unified Candidate Profile
```

---

## Tech Stack

### Backend
- Python
- FastAPI
- Pandas
- Pydantic
- RapidFuzz

### Frontend
- React
- TypeScript
- Vite
- Axios

---

## Project Structure

```
candidate_transformer/

backend/
    app.py
    models/
    parsers/
    services/
    config/

frontend/
    src/

README.md
```

---

## Running the Project

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Backend:

```
http://127.0.0.1:8000
```
<img width="1410" height="360" alt="Screenshot 2026-06-30 121820" src="https://github.com/user-attachments/assets/1666a872-8d9e-42ef-8f3f-8c97d72ee0fb" />

API Docs:

```
http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```
http://localhost:5173
```
<img width="1900" height="866" alt="image" src="https://github.com/user-attachments/assets/1003c353-7b7c-4a17-b496-67f226808592" />


---

## Usage

1. Start the backend.
2. Start the frontend.
3. Upload:
   - `recruiter.csv`
   - `recruiter_notes.txt`
4. Click **Transform**.
5. View the merged candidate profiles with confidence scores and provenance.

---

## Expected Output

Each candidate is transformed into a unified profile containing:

- Personal Information
- Professional Information
- Skills
- Experience
- Education
- Confidence Score
- Provenance

Example:

```text
Johnathan Doe

Email: john.doe@gmail.com
Phone: +919876543210
Experience: 6 Years
Skills: Python, Java, Docker, AWS
Confidence: 95%
```

---

## Assumptions

- Email is the primary identifier for matching candidates.
- Phone number is used as a secondary identifier.
- Name similarity is used when contact details are unavailable.
- Missing fields are allowed and handled gracefully.

---

## Future Improvements

- Resume (PDF/DOCX) parsing
- LinkedIn profile support
- GitHub profile ingestion
- NLP-based information extraction

---

## Author

**Dibjyoti Hota**
