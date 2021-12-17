# Alice Maze Solver

## What are Alize Mazes?

Alice Mazes are puzzles created by Robert Abbott. 

> These are called “Alice” mazes because they recall the scene in ***Alice in Wonderland*** where Alice eats a piece of cake with the sign “Eat Me” and grows larger, then she drinks from a bottle marked “Drink Me” and becomes smaller. These mazes won’t make you larger or smaller, but the distance you travel in a move will get larger or smaller. [^1]

This is an example of the Alice Mazes:

<img src="Examples/example_maze.png" alt="Alice Maze Example" width="150" height="150">

[^1]: https://www.logicmazes.com/alice.html

## Alice Maze Rules

- You start at the block with **red backround colour** and having the **step size** [^2]of **1**.
- You **can** move to the direction of the arrow points to.
- You **cannot** move to the outside of the boundary.
- When stepped on block with **red** arrow , then **step size** increase by 1.
- When stepped on block with **yellow** arrow, then **step size** increase by 1.
- When **goal** block is reached, the game stops.
- The goal is finding solution with the fewest steps[^3].

​	

[^2]: Step size is the number of blocks to move. For example, when step size is 2 and move upward, them move up 2 blocks. 
[^3]: Please note here, the fewest step does not mean the least step size. Step here mean number of movements. For example, if a movement moves up two blocks because step size is 2, step count increases by 1. 



## Maze Representation

