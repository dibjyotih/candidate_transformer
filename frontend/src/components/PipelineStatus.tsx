interface Props{

    running:boolean;

}

export default function PipelineStatus({

    running

}:Props){

    return(

        <div className="pipeline">

            <h2>

                Pipeline

            </h2>

            {

                running ?

                <>

                <p>✔ Parsing</p>

                <p>✔ Validation</p>

                <p>✔ Normalization</p>

                <p>✔ Deduplication</p>

                <p>✔ Conflict Resolution</p>

                <p>✔ Confidence</p>

                </>

                :

                <p>

                    Waiting...

                </p>

            }

        </div>

    );

}