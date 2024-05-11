import './assets/style_dark_web.css'

function  FormData () {
  return (
    <div id="body">
    <div id="container">
     <div id="elems">
                    
                <input id="topic" placeholder="Enter topic" type="text" /><br/>
                <div id="keyword-label">
                    <input id="keyword" placeholder=" Enter Keyword" type="text" />
                    <input id="btn" type="button" value="+" />
                    <div id="site-label">
                        <button id='site'><strong>Scrap</strong></button><br/>
                    </div> 
                </div>
            </div> 
  </div>
  </div>
  )
}

export default FormData
