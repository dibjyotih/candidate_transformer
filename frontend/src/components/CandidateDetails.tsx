import type { Candidate } from "../types/Candidate";

interface Props {
    candidate?: Candidate;
}

export default function CandidateDetails({
    candidate,
}: Props) {

    if (!candidate)
        return (
            <div className="details">

                <h2>Candidate Details</h2>

                <p>Select a candidate</p>

            </div>
        );

    return (
        <div className="details">

            <h2>{candidate.personal.full_name}</h2>

            <hr />

            <h3>Personal</h3>

            <p>
                <b>Email:</b>{" "}
                {candidate.personal.emails.join(", ")}
            </p>

            <p>
                <b>Phone:</b>{" "}
                {candidate.personal.phones.join(", ")}
            </p>

            <p>
                <b>Location:</b>{" "}
                {candidate.personal.location}
            </p>

            <hr />

            <h3>Professional</h3>

            <p>
                <b>Headline:</b>{" "}
                {candidate.professional.headline}
            </p>

            <p>
                <b>Experience:</b>{" "}
                {candidate.professional.years_experience} years
            </p>

            <p>
                <b>Skills</b>
            </p>

            <div className="skills">

                {candidate.professional.skills.map(skill => (

                    <span
                        className="skill"
                        key={skill}
                    >
                        {skill}
                    </span>

                ))}

            </div>

            <hr />

            <h3>Education</h3>

            {candidate.education.map((edu, index) => (

                <div key={index}>

                    <p>{edu.degree}</p>

                    <p>{edu.institution}</p>

                </div>

            ))}

            <hr />

            <h3>Confidence</h3>

            <p>

                {(candidate.metadata.confidence * 100).toFixed(0)}%

            </p>

            <hr />

            <h3>Provenance</h3>

            <div className="provenance">

                {candidate.provenance.map((p, i) => (

                    <div
                        key={i}
                        className="prov-item"
                    >

                        <b>{p.field}</b>

                        <br />

                        Source : {p.source}

                        <br />

                        Method : {p.method}

                    </div>

                ))}

            </div>

        </div>
    );
}