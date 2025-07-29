import React from "react";


const Footer = () => {
    return (
        <div className="card text-center bg-dark text-light">
            <div className="card-header">
                &copy;Defturn (2025)


            </div>
            <div className="card-footer text-body-primary d-flex justify-content-center">
               <div className="mx-2">
                <i className="bi bi-twitter-x"></i>
               </div>
               <div className="mx-2">
                <i className="bi bi-github"></i>
               </div>
               <div className="mx-2">
               <i className="bi bi-instagram"></i>
               </div>
               
               
            </div>
        </div>
    )
}

export default Footer;