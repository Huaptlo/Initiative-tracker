const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({extended: true}));



app.get("/", function(request, respond) {
    // server respond 
    respond.sendFile(__dirname + "/index.html");
});

app.listen(3000, function () {
    // start server on port 3000
    console.log("Server is runnink!");
});