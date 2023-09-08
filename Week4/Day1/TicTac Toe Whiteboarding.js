/*

Use Cases (MVP)

-Truns
-Check every turn for a win case
-Win, tide condition
-Players
-Game board
-Start game
-End game
-Display matrix
-Ask the player Cordinates


Clases

Actors    
Player   
--------------      
Name:string      
-------------
  

Clases
gameBoard
------------
matrix:array of array
------------
checkForWin()
updateMatrix()

Relationships:
    gameBoard : Player :: 1:N

*/

/// JavaScript

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function askName() {
    rl.question('Please input your name\n', (answer) => {
        console.log(`Hello ${answer}!`);
        rl.close();
    });
}

askName();


class Player {
  constructor(name, operator) {
    this.name = name
    this.operator = operator
  }
  getOperator() => {
    this.operator
  }

class Board {
  constructor() {
    this.matrix = [
      ['_','_','_'],          
      ['_','_','_'],
      ['_','_','_'],
    ]
  }
  updateMatrix(x,y) => {
    if(this.matrix[x][y] === '_'){
      this.matrix[x][y]= Player.getOperator()
      checkForWin()
    } else {
      console.log('Space already taken')
    }
  }
  checkForWin() => {
    let checkSet = new Set(Player.getOperator(), this.matix[x][y])
    for (let x = 0;x < this.matrix.length-1; x++)
      for(let y = 0; y < this.matrix[x].length-1; y++)
        if()
  }
  
}

--> y+1
['0,0','0,1','_'],          
['1,0','_','_'],
['_','_','_'],

|
\/
x+1