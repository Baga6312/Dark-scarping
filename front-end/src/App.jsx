import FormData from  './components/FormData'
import DarkPageScrap from './components/DarkPageScrap'
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';

function App() {

  return (
  <div>
     <Router>
      <div className="login">
        <Routes>
          <Route path="/" element={<FormData/>}/>
          <Route path="/Scrapping-page" element={<DarkPageScrap/>}/>
        </Routes>
      </div>
    </Router>  
  </div>
  )
}

export default App
