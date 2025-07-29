import axios from 'axios'

const API = 'https://phishing-app-41sr.onrender.com'

export const postURL = async(data) => {
    return await axios.post(`${API}/predict`, data, {headers: {'Content-Type' : 'application/json'}})
} 