import React, {useState} from "react";
import { postURL } from "../api";

function Search({button}) {

    const [urlloc, setURLLoc] = useState({url:''})

    function handleChange(e) {
        setURLLoc({...urlloc, [e.target.name]:e.target.value})
        // console.log(urlloc)
    }

    function handleSubmit(e){
        e.preventDefault();

    }

    return (

        <div className="container">
            <form action="" method="post">
                <div className="d-flex justify-content-center">
                    <input type="text" className="mx-3 px-4 rounded-3 " value={urlloc.url}  name="url" onChange={handleChange} style={{width:'350px', border:'2px solid black'}}  placeholder="https://example.com" required/>
                    {button}
                </div>
                
            </form>
        </div>
    );
}

export default Search;