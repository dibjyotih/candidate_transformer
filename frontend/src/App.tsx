import { useState } from "react";
import axios from "./services/api";

import UploadPanel from "./components/UploadPanel";
import CandidateList from "./components/CandidateList";
import CandidateDetails from "./components/CandidateDetails";

import type { Candidate } from "./types/Candidate";

import "./styles/app.css";

export default function App() {

    const [candidates, setCandidates] = useState<Candidate[]>([]);
    const [selected, setSelected] = useState<Candidate | undefined>(undefined);
    const [loading, setLoading] = useState(false);

    async function transform(csv: File, notes: File) {

        const formData = new FormData();

        formData.append("csv", csv);
        formData.append("notes", notes);

        setLoading(true);

        try {

            const response = await axios.post(
                "/transform",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            setCandidates(response.data);

            if(response.data.length>0)
                setSelected(response.data[0]);

        } catch (err) {

            alert("Transformation Failed");

            console.log(err);

        }

        setLoading(false);

    }

    return (

        <div className="container">

            <h1>Candidate Data Transformer</h1>

            <UploadPanel onSubmit={transform}/>

            {loading && <p>Processing...</p>}

            <div className="layout">

                <CandidateList

                    candidates={candidates}

                    onSelect={setSelected}

                />

                <CandidateDetails

                    candidate={selected}

                />

            </div>

        </div>

    );

}