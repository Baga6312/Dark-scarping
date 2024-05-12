const express = require("express")
const cors =require("cors")
const app = express()
require("dotenv").config()
const {exec } =require ("child_process")
const PORT = process.env.port

app.use(cors())
app.get('/command' , async (req , res)=> { 
    const data =  req.query.info.split(" ") 
    console.log( data) 
    // const drama = exec(`python3 scraping.py ${data[0]} ${data[1]} ${data[2]}   ` , (stderr , stdout ,err ) => { 
    const drama = exec(`python3 scraping.py ` , (stderr , stdout ,err ) => { 
        if (stderr) { 
            console.log(stderr)
        }
        if ( stdout ) {
            console.log(stdout )
        }
        if (err) { 
            console.log(err)
        }        
       res.send({message : data})
    })
})

app.listen(PORT || 5001 , (data)=> { 
    console.log(`listening on port ${PORT}`)
})