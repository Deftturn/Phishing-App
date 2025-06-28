import Search from "../Component/Search";
// import Card from "../Component/Card";
// import { postURL } from "../api";


function HomePage() {

    // function handleSubmit(e) {
    //     e.preventDefault()
        
    // }


    return (
        <div className="container mt-5">
            <h2> Which URL Do You Have In Mind 🤔 ?</h2>
            <div className="card p-3 m-3 border-0">
                <div className="card-body">
                    <Search button={<button className="btn btn-dark">predict</button>}/>
                    <div className="card mt-4 p-2 border-0">
                    
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomePage;