import type { Candidate } from "../types/Candidate";

interface Props {
    candidate: Candidate;
    onSelect: (candidate: Candidate) => void;
}

export default function CandidateCard({
    candidate,
    onSelect,
}: Props) {
    return (
        <div
            className="candidate-card"
            onClick={() => onSelect(candidate)}
        >
            <h3>{candidate.personal.full_name}</h3>

            <p>{candidate.professional.headline}</p>

            <p>
                ⭐ Confidence:{" "}
                {(candidate.metadata.confidence * 100).toFixed(0)}%
            </p>
        </div>
    );
}