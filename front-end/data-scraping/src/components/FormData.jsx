import {useEffect, useState} from 'react'
import Service from '../components/service'

function  FormData () {
  const [data, setData ] = useState('')
  const [userData , setUserData] = useState('')
  const serv = Service()

  const handleSubmit=async (e , data) => { 
      e.preventDefault()
      const dululu =await  serv.searchForData()
      setUserData(dululu.message)
  }
  return (
  <div>
      <form onSubmit={handleSubmit}>
        <div>
            <p>insert ur email bitch</p>
            <input type="text" onChange={(e)=> {setData(e.target.value)}}/><br/><br/>
            <input type="submit" value="search"  />
            {!userData ? <p>u r good fam fr</p>: <p>uve been doxed by the skibidi council </p>}

       </div>
    </form>
  </div>
  )
}

export default FormData
