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
const chrList = [
  { name: "Jorgovich", initiative: 40 },
  { name: "Robert", initiative: 2 },
  { name: "Peikko", initiative: 69 },
];

app.get('/', (req, res) => {
  //servu auki
  res.render('index', { chrList });
});

app.post('/', (req, res) => {

  //luodaan hahmo objecti
  let newCharacter = {
    name: req.body.chrName,
    initiative: parseInt(req.body.chrIniti)
  }
  chrList.push(newCharacter);
  // lisätään hahmo listaan
  chrList.sort((a, b) => b.initiative - a.initiative);
  // sortataan lista initiative muuttujan mukaan
  res.redirect('/');
});

app.listen(3000, () => {
  console.log('Server runnink!');
});
