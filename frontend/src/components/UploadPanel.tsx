import { useState } from "react";

interface Props{

    onSubmit:(csv:File,notes:File)=>void;

}

export default function UploadPanel({

    onSubmit

}:Props){

    const[csv,setCsv]=useState<File>();

    const[notes,setNotes]=useState<File>();

    return(

        <div className="upload-panel">

            <h2>

                Upload Files

            </h2>

            <input

            type="file"

            accept=".csv"

            onChange={(e)=>{

                if(e.target.files)

                    setCsv(e.target.files[0]);

            }}

            />

            <input

            type="file"

            accept=".txt"

            onChange={(e)=>{

                if(e.target.files)

                    setNotes(e.target.files[0]);

            }}

            />

            <button

            onClick={()=>{

                if(csv && notes)

                    onSubmit(csv,notes);

            }}

            >

            Transform

            </button>

        </div>

    );

}