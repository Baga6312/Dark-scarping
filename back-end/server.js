const express = require("express")
const cors =require("cors")
const app = express()
require("dotenv").config()
const {exec } =require ("child_process")
const PORT = process.env.port

app.use(cors())
app.get('/command' , async (req , res)=> { 
    const data = req.query.data 
    const drama = exec(`echo $USER` , (stderr , stdout ,err ) => { 
        if (stderr) { 
            console.log(stderr)
        }
        if ( stdout ) {
            console.log(stdout )
        }
        if (err) { 
            console.log(err)
        }
        res.send({message : stdout})
    })
})

app.listen(PORT || 5001 , (data)=> { 
    console.log(`listening on port ${PORT}`)
})