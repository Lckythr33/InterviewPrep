/**

Connect N Ropes with Minimum Cost

Given n ropes of different lengths represented by an array of integers, connect them all into a single rope in a way that minimizes the cost of connecting them.

The cost of connecting two ropes is equal to sum of their lengths. We want to minimize the cost of connecting all the ropes.

9 + 6 = 15


Input: ropes, [Integer]
Output: Integer

In: [4, 3, 2, 6]
Out: 29

In:[25,23,15,13,1,0,1,2,4]

0,1,1,2,4,13,15,23,25

1


sum=0
2+3
cost=5
sum=sum+cost

2 3
cost=5


5
4
cost=9

4
6
cost=10

total=29


                        4
                    \
6
                      

extractMin()

4.                      
3
cost=7

7
6
cost=13

13
2
cost=15

In: [4, 3, 2, 6]

const minHeap = new Heap();
const maxHeap = new Heap(Heap.maxComparator);

minHeap.init([5, 18, 1]);
minHeap.push(2);
console.log(minHeap.peek()); //> 1
console.log(minHeap.pop()); //> 1
console.log(minHeap.peek()); //> 2

PseudoCode:
sum=0
1. Create a min heap from the array
2. Take the minimum value of the array from the min heap extractMin()
//Restructure the heap
Get firstmin = 2,  4, 6
3.Repeat step 2.
Get secondmin = 3,  5  , 9

4. combinedrope= firstmin+secondmin  sum= sum+5, sum+9, sum+15
    Put the combined rope in the min heap, recreate min heap.
[4,5,6], [6,9], [15]

Feel free to use abstraction (you don't have to actually implement the methods of the heap until later)

Space: O(1)
Time: O(n)+nlog(n) = nlog(n)
*/
heap = require('heap-js');

function calculateCost(ropes){
  if(ropes.length==1) return ropes[0];
  let sum=0;
  let minheap = new heap.Heap(); // O(n)
  minheap.init(ropes);
  while(minheap.size()>1){
    const firstmin = minheap.pop(); // O(logn)
    const secondmin= minheap.pop(); //
    const combined_rope = firstmin+secondmin;
    sum+=combined_rope;
    minheap.push(combined_rope);
  }
  return sum;
}

console.log(calculateCost([1]))
// size()
