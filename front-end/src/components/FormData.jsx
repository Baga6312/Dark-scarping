import { useNavigate } from 'react-router-dom';
import '../assets/styel_home.css'
function  FormData () {

  const navigate = useNavigate()
    
  const handleDark = (e ) => { 
    e.preventDefault();
    navigate('/Dark-Scrapping-page');
  }

  const handleGithub = (e ) => { 
    e.preventDefault();
    navigate('/Github-Scrapping-page');
  }
  return (

    <div id="body">
    <div id="container">
    <div id="logo">
		<h1 >Dark Gate</h1>
      <img id="image" src='../src/assets/wp11184521-black-anime-galaxy-wallpapers.jpg'/>
      <p>Because you have the right to be aware</p>
        </div>
        <div id="buttons">
            <span><input className="signin-btn" type="button" value="GitHub Scrapper"  onClick={handleGithub}/></span><br/><br/>
            <span><input className="signup-btn" type="button" value="DarkWeb Scrapper" onClick={handleDark} /></span><br/><br/>
        </div>
  </div>
  </div>
  )
}

export default FormData
