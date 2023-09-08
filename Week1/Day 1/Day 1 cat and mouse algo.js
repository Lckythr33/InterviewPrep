/*

There is a board with squares (say 10 x 10 matrix) and one random square on the matrix is marked as exit. Some squares in the board are also grayed out which means that box is not available to be visited.

There is a mouse that can only move one block at a time and Cat that can move 2 blocks at a time.

If cat reaches mouse first, then cat wins. But if mouse reached exit square first then mouse wins.
Given starting position of Mouse and Cat, find out if Mouse can exit safely or will die.


input: matrix(int[][]), timeout period as well (int) 

output: true (mouse can exit alive), false (cat catches mouse, or mouse starves) 


input: 

[
  [0,3,1,0,0],
  [1,0,0,0,0],
  [0,0,0,0,1],
  [1,1,0,1,1],
  [0,0,2,9,0]
]

output: true 


input: 

[
  [3,0,1,0,0],
  [1,0,0,0,0],
  [0,0,2,0,1],
  [1,1,0,1,1],
  [0,0,0,9,0]
]

output: true 


input: 

[
  [0,0,1,0,0],
  [1,0,0,0,0],
  [0,0,2,0,1],
  [1,1,0,1,1],
  [0,0,3,9,0]
]

output: false 


input: 

[
  [0,0,1,0,0],
  [1,0,0,0,0],
  [0,0,0,0,1],
  [1,1,0,1,1],
  [3,2,0,9,0]
]

output: false 

time: None
space: None


notes: 

- cat - can move two spaces at a time
- mouse - can move one space at a time 
- 1s - walls 
- 0s - empty spaces
- 3 - cat 
- 2 - mouse 
- 9 - exit 
- if mouse and cat reaches exit block at same time, mouse lives 
- mouse and cat can move vertically and horizontally



x ---> 
[
  [0,2,1,0,0],
  [1,0,0,0,0],
  [0,0,0,0,1],
  [1,1,0,1,1],
  [3,2,0,9,0]
]      
y
|
|
v



visited = {
  "1_4",
  "2_4"
}


queue = 
------------------------------------------------------------------------------
[2,3,2],[3,4,2]
------------------------------------------------------------------------------

current = [2,4,1]
    
                                        
observations: 
- find shortest distance to exit for both cat and mouse 

- mouse (2), cat (4) --> mouse lives 
- mouse (2), cat (3) --> mouse dies

- use breadth-first traversal to find shortest paths 
  - create a queue
  - enqueue each starting point (cat or mouse) 
  - spread outwards from starting point 
  - when exit is encountered, record that distance for each animal

- if cat moves >= 2 * mouse moves, mouse lives (return true)
- otherwise, mouse dies (return false )



*/

const canTravel = (matrix, x, y, visited) => {
    if (x < 0 || y < 0 || x >= matrix[0].length || y >= matrix.length) {
      return false;
    }
    if (matrix[y][x] === 1) {
      return false;
    }
    let key = x + '_' + y;
    if (visited.has(key)) {
      return false;
    }
  
    return true;
  }
  
  
  const bfs = (matrix, startX, startY) => {
    const queue = [];
    queue.push([startX, startY, 0]);
    const visited = new Set();
  
    let x;
    let y;
    let distance;
  
    while (queue.length > 0) {
      [x, y, distance] = queue.shift();
  
      if (matrix[y][x] === 9) {
        return distance;
      }
  
      // north
      if (canTravel(matrix, x, y - 1, visited)) {
        let key = x + '_' + (y-1);
        visited.add(key);
        queue.push([x, y - 1, distance + 1]);
      }
      
      // south 
      if (canTravel(matrix, x, y + 1, visited)) {
        let key = x + '_' + (y+1);
        visited.add(key);
        queue.push([x, y + 1, distance + 1]);
      }
      
      // east
      if (canTravel(matrix, x + 1, y, visited)) {
        let key = (x+1) + '_' + y;
        visited.add(key);
        queue.push([x + 1, y, distance + 1]);
      }
      
      // west
      if (canTravel(matrix, x - 1, y, visited)) {
        let key = (x-1) + '_' + y;
        visited.add(key);
        queue.push([x - 1, y, distance + 1]);
      }
    }
  
    return 0;
  }
  
  
  const doesMouseLive = (matrix, mouseLifespan) => {
    let catDistance = 0;
    let mouseDistance = 0;
    
    for (let y = 0; y < matrix.length; y++) {
      for (let x = 0; x < matrix[0].length; x++) {
        if (matrix[y][x] === 3) {
          catDistance = bfs(matrix, x, y); 
        }
        if (matrix[y][x] === 2) {
          mouseDistance = bfs(matrix, x, y);
        }
      }
    }
  
    console.log("MOUSE DISTANCE: ", mouseDistance);
    console.log("CAT DISTANCE: ", catDistance);
  
    if (mouseDistance === 0) {
      return false;
    }
  
    if (mouseDistance > mouseLifespan) {
      return false;
    }
  
    if (catDistance >= (2 * mouseDistance)) {
      return true;
    } else {
      return false;
    }
  }
  
  let test = [
    [0,3,1,0,0],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [1,1,0,1,1],
    [0,0,2,9,0]
  ]
  
  console.log(doesMouseLive(test, 10));