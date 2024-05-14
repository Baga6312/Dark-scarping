import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'
import '../assets/style_dark_web.css'
import Service from './service.jsx'

function GitHubScrapper() {
  const [divs, setDivs] = useState([]);
  const [inputValue, setInputValue] = useState([{ value: '' }]); 
  const baseurl = 'http://localhost:5001/command'
  const navigate = useNavigate()
  const service = Service()

  
  const search = async () => {
    console.log(inputValue);
    const params = {};
    for (let i = 0; i < inputValue.length; i++) {
      params[`key${i}`] = inputValue[i].value;
    }
  
    try {
      const response = await axios.get(baseurl, { params });
      console.log(response.data.message);
    } catch (error) {
      console.error('Error searching:', error);
    }
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
          onChange={(e) => handleInputChange(prevDivs.length, e.target.value)}
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


  const handleInputChange = (index, value) => {
    setInputValue((prevInputValues) => {
      const newInputValues = [...prevInputValues];
      newInputValues[index] = { value };
      return newInputValues;
    });
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
              onChange={(e)=> handleInputChange( inputValue.length -1  , e.target.value)}
              type="text"
            />
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
