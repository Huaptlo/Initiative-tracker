//importataan moduulit
const express = require("express");

// otetaan käyttöön
const app = express();

// käytetään ejs tiedostoja html sijaan
app.set('view engine', 'ejs');

// aktivoidaan body parser ja staattiset sivut
app.use(express.urlencoded({extended: true}));
app.use(express.static("public"));

let chrList = [];

app.get("/", function(req, res) {
    // server respond
    res.render("index", {characterList: chrList});
});

app.post("/", function(req, res) {
    let chrName = req.body.chrName;
    let chrInit = req.body.chrIniti;

    // luodaan hahmo objecti
    let newCharacter = {
        name: chrName,
        initiative: chrInit
    };

    chrList = chrList.sort();
    chrList.push(newCharacter);
    res.redirect("/");
});

app.listen(3000, function () {
    // start server on port 3000
    console.log("Server is runnink!");
});