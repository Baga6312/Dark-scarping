import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../assets/style_dark_web.css'
import Service from './service.jsx'

function GitHubScrapper() {
  const [data, setData] = useState("")
  const [input1, setInput1] = useState("")
  const [divs, setDivs] = useState([]);
  const [inputValue , setInputValue] =  useState([])
  const navigate = useNavigate()
  const service = Service()

  const search = () => {
    const Data = service.searchForData()
  }

  const menu = (e) => {
    e.preventDefault();
    navigate('/home');
  }

  const addNewDiv = () => {
    setDivs(prevDivs => [
      ...prevDivs,
      <div key={prevDivs.length + 1} id='keyword-label-1'>
        <input 
          id='keyword-1' 
          className='keyword-class'
          value={inputValue} 
          onChange={(e)=> setInputValue(e.target.value)}
          placeholder=" Enter Keyword" 
          type="text"
        />
        <input 
          id='btn-1'
          type="button" 
          value="+" 
          onClick={addNewDiv}
        />
      </div>
    ]);
  };

  return (
    <div id="body">
      <div id="container">
        <div id="elems">
          <h1>Welcome to GitHub Scrapping </h1>
          <input id="topic" placeholder="Enter topic" type="text" /><br />
          <div id="keyword-label">
            <input
              id="keyword"
              placeholder=" Enter Keyword"
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)} />
            <input
              id="btn"
              type="button"
              value="+"
              onClick={addNewDiv}
            />
          {divs}






            <div id="site-label">
              <button
                id='site'
                onClick={search}> 
                  <strong>Scrap</strong>
              </button><br/>
            </div>

            <div id="site-label">
              <button id='site' onClick={menu}><strong>Menu</strong></button><br/>
            </div>
          </div>
        </div>
        <img id="image" src='../src/assets/wp11184521-black-anime-galaxy-wallpapers.jpg' alt="background" />
      </div>
    </div>
  )
}

export default GitHubScrapper;
