import axios from 'axios'
import { useState } from 'react'

function Service() {
const baseurl = 'http://localhost:5001/command'
const [data ,setData ] = useState([])
    const searchForData = async (data) => { 
        // const response = await axios.get(`${baseurl}` , {info : data })
        // setData(response.data)
        // return response.data
    }
    const getData = () => { 
        return [
            localStorage.getItem("data")
        ]
    }
    return { 
        getData , 
        searchForData,
    }

}

export default  Service ;
