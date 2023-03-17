//importataan moduulit
const express = require('express');
//otetaan käyttöön express
const app = express();

// käytetään ejs tiedostoja html sijaan
app.set('view engine', 'ejs');
// aktivoidaan bodyparser ja staattiset tiedostot
app.use(express.urlencoded({ extended: false }));
app.use(express.static("public"));

//luodaan uusi lista hahmoille
const chrList = [];

app.get('/', (req, res) => {
  // renderoidaan servu
  res.render('index', { chrList });
});

app.post('/chr', (req, res) => {

  //luodaan hahmo objecti
  let newCharacter = {
    name: req.body.chrName,
    initiative: req.body.chrIniti
  }
  
  chrList.push(newCharacter);
  // lisätään hahmo listaan
  chrList.sort((a, b) => b.initiative - a.initiative);
  // sortataan lista initiative muuttujan mukaan
  res.redirect('/');
});


//TODO clear func
app.post("/clear", (req, res) => {
  
  while(chrList.length > 0) {
    chrList.pop()
  }

  res.redirect("/");
});

app.listen(3000, () => {
  console.log('Server runnink!');
});
