import Search from "../Component/Search";
// import Card from "../Component/Card";
import { postURL } from "../api";
import { useState } from "react";
import Chart from "../Component/Chart";

function HomePage() {

    // function handleSubmit(e) {
    //     e.preventDefault()
        
    // }

    const [input, setInput] = useState({url:''})
    const [output, setOutput] = useState({predictions:''})
    const [hasSubmitted, sethasSubmitted] = useState(false)

    const handleChange = (e) => {
        setInput({...input, [e.target.name] : e.target.value})
        
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        try{
            const res = postURL(input)
            
            setOutput({...output, predictions : (await res).data.predictions})
            sethasSubmitted(true)
            console.log((await res).data)
        }catch (e) {
            console.error(e)
        }
    }

    


    return (
        <div className="container mt-5 ">
            <h2 className="text-light"> Which URL Do You Have In Mind 🤔 ?</h2>
            <div className="card p-3 m-3 border-0 bg-back">
                <div className="card-body">
                    <Search value={input.url} onChange={handleChange} onSubmit={handleSubmit}/>
                </div>
                {hasSubmitted && output && (
                    <div className="mt-4 p-2 border-0">
                        {output.predictions === '-1' ? <p className="p-4 rounded bg-danger">Prediction: Phishing URL</p> : <p className="p-4 rounded bg-success text-light">Prediction: Legitimate</p>}
                    </div>
                )}

                <div className="d-flex justify-content-center">
                    <Chart/>
                </div>
            </div>
        </div>
    )
}

export default HomePage;