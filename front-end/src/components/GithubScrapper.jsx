import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../assets/style_dark_web.css'
import   Service from './service.jsx'

function  GitHubScrapper() {
  const [data , setData ] = useState("")
  const [input1 , setInput1 ] =  useState("")
  const service = Service()
  const navigate = useNavigate()
    const search = () => { 
      const Data = service.searchForData() 
      // setData(Data)
      // console.log(data)
    }
    const menu = (e) => { 
        e.preventDefault();
        navigate('/home');
    }

  return (
    <div id="body">
        <div id="container">
        <div id="elems">
            <h1>Welcome to GitHub Scrapping </h1>
                    <input id="topic" placeholder="Enter topic" type="text" /><br/>
                    <div id="keyword-label">
                        <input 
                            id="keyword" 
                            placeholder=" Enter Keyword" 
                            type="text"
                            value ={input1} 
                            onChange={(e)=> setInput1(e.target.value)} />
                        <input id="btn" type="button" value="+" />
                            <div id="site-label">
                                <button id='site' onClick={search()}><strong>Scrap</strong></button><br/>
                            </div> 
                            <div id="site-label">
                                <button id='site' onClick={menu}><strong>Menu</strong></button><br/>
                            </div> 
                    </div>
                <img id="image" src='../src/assets/wp11184521-black-anime-galaxy-wallpapers.jpg'/>
        </div> 
        </div>
    </div>
  )
}

export default GitHubScrapper
