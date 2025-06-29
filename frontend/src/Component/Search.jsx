function Search({url, onChange, onSubmit}) {

   

    return (

        <div className="container">
            <form action="" method="post" onSubmit={onSubmit}>
                <div className="d-flex justify-content-center">
                    <input type="text" className="mx-3 px-4 rounded-3 " value={url}  name="url" onChange={onChange} style={{width:'350px', border:'2px solid black'}}  placeholder="https://example.com" required/>
                    <button className="btn btn-dark">predict</button>
                </div>
                
            </form>
        </div>
    );
}

export default Search;