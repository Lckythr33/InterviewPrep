

const islandPerimeter = function(grid){      
    let perimeter = 0
    
    for(let row = 0; row < grid.length; row++){
        for(let col = 0; col < grid[row].length; col++){
            
            if(grid[row][col] === 1){
                perimeter+=4
                
                if(row > 0 && grid[row-1][col]===1){perimeter-=2}
                
                if(col > 0 && grid[row][col-1] === 1){perimeter-=2}
            }
        }
    }
    return perimeter 
}


  /* solution #2

                      let perimeter = 0
    
    let rowSize = grid.length;
    let colSize = grid[0].length;
    
    for(let row = 0; row < rowSize; row++){
        for(col = 0; col < colSize; col++){
            
            if(grid[row][col]===1){
                
                let up = row === 0 ? 0 : grid[row-1][col]
                let down = row === rowSize-1 ? 0 : grid[row+1][col]
                let left = col === 0 ? 0 : grid[row][col-1]
                let right = col === colSize-1 ? 0 : grid[row][col+1]
                
                if(up === 0) perimeter++
                if(down === 0) perimeter++
                if(left === 0) perimeter++
                if(right === 0) perimeter++
            }
        }
    }
    
    return perimeter
                  
      
*/