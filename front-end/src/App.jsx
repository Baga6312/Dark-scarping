import FormData from  './components/FormData'
import DarkPageScrap from './components/DarkPageScrap'
import GitHubScrapper from './components/GithubScrapper'
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';

function App() {

  return (
  <div>
     <Router>
      <div className="login">
        <Routes>
          <Route path="/" element={<FormData/>}/>
          <Route path="/Dark-Scrapping-page" element={<DarkPageScrap/>}/>
          <Route path="/Github-Scrapping-page" element={<GitHubScrapper/>}/>
        </Routes>
      </div>
    </Router>  
  </div>
  )
}

export default App
