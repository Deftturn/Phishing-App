

function Card(prop) {
    return (

        <div className="card rounded-4 bg-light p-4 my-2">
            <div className="row">
                <div className="card-title">{prop.title}</div>
                <p> url: {prop.url} </p>
                <p className="">Classification:  {prop.predict}</p>
            </div>
        </div>
    );
}

export default Card;