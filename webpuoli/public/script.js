const chrList = document.getElementById("table1");
const startEnc = document.getElementById("startEncounter");
const endEnc = document.getElementById("endEncounter");
const nextBtn = document.getElementById("nextButton");

let numOfChr = Number(chrList.rows.length);


startEnc.addEventListener("click", () => {
    turnCount = 0;
    endEnc.removeAttribute("disabled");
    nextBtn.removeAttribute("disabled");
    chrList.rows[turnCount].classList.add("active");
});

endEnc.addEventListener("click", () => {
    for(let i = 0; i < numOfChr; i++) {
        chrList.rows[i].classList.remove("active");
    };
    nextBtn.setAttribute("disabled","");
    endEnc.setAttribute("disabled", "");

    //isEncounter = false;
});

nextBtn.addEventListener("click", () => {
    // käydään hahmo listää läpi
    chrList.rows[turnCount].classList.remove("active");
    
    turnCount += 1;
    if(turnCount > numOfChr -1) {
        turnCount = 0;
    };
    // jos vuoro ylittää hahmolistan pituuden niin nollataan arvo
    //console.log(turnCount);
    chrList.rows[turnCount].classList.add("active");
});

