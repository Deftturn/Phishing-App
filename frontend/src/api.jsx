import axios from 'axios'

const API = 'http://localhost:3214'

export const postURL = async(data) => {
    return await axios.post(`${API}/predict`, data, {headers: {'Content-Type' : 'application/json'}})
} 