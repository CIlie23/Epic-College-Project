const sounds = ['static/sound1.wav', 'static/sound2.wav', 'static/sound3.wav']; // array
let nivel = 0;
//let highestScore = 0;
let sequence = [];
let userSequence = [];
let isUserTurn = false;

//-----------Start game--------------------------------------
function startGame(){
  document.getElementById('startButton').disabled = true;
  //document.getElementById('nextButton').disabled = false;
  playRandomSound();
  displayVariable();
}

function nextPuzzle(){
  document.getElementById('nextButton').disabled = true;
  console.log('next puzzle');
  playRandomSound();
  displayVariable();
}

function nextLevel(){
  nivel += 1;
}

function displayVariable(){
  const nivelCounter = document.getElementById('nivelCounter');
  nivelCounter.textContent = nivel;
}
//-----------Sounds-------------------------------------------
function playSoundOne(){
  checkSound('static/sound1.wav');
  var snd = new Audio("static/sound1.wav");
  snd.play();
}

function playSoundTwo(){
  checkSound('static/sound2.wav');
  var snd = new Audio("static/sound2.wav");
  snd.play();
}

function playSoundThree(){
  checkSound('static/sound3.wav');
  var snd = new Audio("static/sound3.wav");
  snd.play();
}

function playSound(filename) {
  var snd = new Audio(filename);
  snd.play();
}

//-----------Gameplay  loop--------------------------------------
function checkSound(expectedSound) {
  if (expectedSound === lastPlayedSound) {
    console.log('Corect! Sunetul auzit coincide cu sunetul butonului.');
    document.getElementById('nextButton').disabled = false;
    nextLevel()
    
    if (nivel > highestScore) {
      highestScore = nivel;
      updateHighestScoreDisplay();
    }

  } else {
    console.log('Greșit! Sunetul auzit nu coincide cu sunetul butonului.');
    document.getElementById('startButton').disabled = false;
    document.getElementById('nextButton').disabled = true;
    nivel = 0;
  }
}

let lastPlayedSound;

function playRandomSound() {
  const randomIndex = Math.floor(Math.random() * sounds.length);
  const randomSound = sounds[randomIndex];
  playSound(randomSound);
  lastPlayedSound = randomSound;
}

//-----------Saving--------------------------------------------------
function updateHighestScoreDisplay() {
  const highestScoreDisplay = document.getElementById('highestScore');
  highestScoreDisplay.textContent = highestScore;
  updateHighestScore(nivel) 
}

function updateHighestScore(nivel) {//this saves the score, yay!!
  fetch(`/save_score/${nivel}`, { method: 'GET' })
      .then(response => {
          if (!response.ok) {
              console.error('Failed to save score');
          }
      })
      .catch(error => console.error('Error:', error));
}


