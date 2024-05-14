import axios from 'axios'
import { useState } from 'react'

function Service() {
const [data ,setData ] = useState([])

    const searchForData = async (data) => { 
        return response.data
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
