import type { Candidate } from "../types/Candidate";
import CandidateCard from "./CandidateCard";

interface Props {
    candidates: Candidate[];
    onSelect: (candidate: Candidate) => void;
}

export default function CandidateList({
    candidates,
    onSelect,
}: Props) {
    return (
        <div className="candidate-list">

            <h2>Candidates</h2>

            {candidates.length === 0 && (
                <p>No Candidates</p>
            )}

            {candidates.map((candidate) => (
                <CandidateCard
                    key={candidate.candidate_id}
                    candidate={candidate}
                    onSelect={onSelect}
                />
            ))}
        </div>
    );
}