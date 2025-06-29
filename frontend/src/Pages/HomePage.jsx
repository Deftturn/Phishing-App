import Search from "../Component/Search";
// import Card from "../Component/Card";
import { postURL } from "../api";
import { useState } from "react";

function HomePage() {

    // function handleSubmit(e) {
    //     e.preventDefault()
        
    // }

    const [input, setInput] = useState({url:''})
    const [output, setOutput] = useState({url:''})
    const [hasSubmitted, sethasSubmitted] = useState(false)

    const handleChange = (e) => {
        setInput({...input, [e.target.name] : e.target.value})
        
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        try{
            const res = postURL(input)
            
            setOutput({...output, url : (await res).data.prediction})
            sethasSubmitted(true)
            console.log((await res).data)
        }catch (e) {
            console.error(e)
        }
    }

    


    return (
        <div className="container mt-5">
            <h2> Which URL Do You Have In Mind 🤔 ?</h2>
            <div className="card p-3 m-3 border-0">
                <div className="card-body">
                    <Search value={input.url} onChange={handleChange} onSubmit={handleSubmit}/>
                </div>
                {hasSubmitted && output && (
                    <div className="card mt-4 p-2 border-0">
                        {output.url === -1 ? <p className="p-4 rounded bg-danger">Prediction: Phishing URL</p> : <p className="p-4 rounded bg-success text-light">Prediction: Legitimate</p>}
                    </div>
                )}
            </div>
        </div>
    )
}

export default HomePage;