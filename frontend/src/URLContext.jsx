/* eslint-disable react-refresh/only-export-components */
import React, { createContext, useState } from "react";

export const URLContext = createContext();

export const URLProvider = ({children}) => {
    const [url, setUrl] = useState({url: ''});

    return(
        <URLContext.Provider value={{url, setUrl}}>
            {children}
        </URLContext.Provider>
    )
}