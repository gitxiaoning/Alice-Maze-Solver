# Alice Maze Solver

## What are Alize Mazes?

Alice Mazes are puzzles created by Robert Abbott. 

> These are called “Alice” mazes because they recall the scene in ***Alice in Wonderland*** where Alice eats a piece of cake with the sign “Eat Me” and grows larger, then she drinks from a bottle marked “Drink Me” and becomes smaller. These mazes won’t make you larger or smaller, but the distance you travel in a move will get larger or smaller. [^1]

This is an example of the Alice Mazes:

<img src="Examples/example_maze.png" alt="Alice Maze Example" width="150" height="150">

[^1]: https://www.logicmazes.com/alice.html

## Alice Maze Rules

- You start at the block with **red backround colour** and having the **step size** [^2]of **1**.
- You **can** move to the direction of the arrow points to, and you **cannot** move to the outside of the boundary.
- When stepped on the block with **red** arrow , then **step size** increase by 1.
- When stepped on the block with **yellow** arrow, then **step size** increase by 1.
- When **goal** block is stepped, the game stops.
- The goal is finding solution with the **fewest steps**[^3].

​	

[^2]: Step size is the number of blocks to move. For example, when step size is 2 and move upward, them move up 2 blocks. 
[^3]: Please note here, the fewest steps do not mean the least step size. Step here mean number of movements. For example, if a movement moves up two blocks because step size is 2, step count increases by 1. 



## Maze Representation

The file stores maze in a csv format[^4]:

1. - The first line is a integer which represents the size of maze: let size of

     maze be n.

   - The second line has two numbers and each represents the x and y coordi-

     nate of the initial(staring) position.

   - The third line has two numbers and each represents the x and y coordinate of the goal position.

     From forth line to (4 + n)th line, contains n × n pairs of data. Each pair has a letter and a number: letter, number. Letters are only from the set: {R,Y,B,G,N}, where R stands for Red Arrow, Y stands for Yellow Arrow, B stands for Black Arrow, G stands for Goal, and N stands for no arrows. The numbers are direction of arrows:

     <img src="Figures/direction.png" alt="Alice Maze Example" width="160" height="150">

     Each number represents a direction as the image shown and 0 represents no directions. If there are multiple arrows at the same location, then on number is concatenated to one other. i.e. If there are directions of top(2) and right(4). Then 24 will represent it.

2. - After the file is loaded, a tuple will be returned and stores all information: 

     `(maze size,initial x,initial y,maze grid,final x,final y)`

     - –  `maze_size`: stores the size of the maze.
     - –  `initial_x`: the initial location (x-axis) where Alice is at.
     - –  `initial_y`: the initial location (y-axis) where Alice is at.
     - –  `final_x`: the initial location (x-axis).
     - –  `inal_y`: the initial location (y-axis).
     - –  `maze_grid`: is a n × n 2D list represents the maze. Every (i, j) entry in maze grid, where i, j ∈ N and i, j < n, stores the arrow informa- tion on each respective location. i.e. the (0,0) entry of maze grid represents the first row’s first block; (1, 0) entry of maze grid repre- sents the second row’s first block; (n − 1, n − 1) entry of maze grid represents the nth row’s nth block. Within each block, it stores a list has five items:
       - `arrow_colour`: stores the arrow colour of current location
       - `arrow_direction_code`: stores the code represents the arrow’s di- rection; need to call code2direction() for interchanging the code to actual direction.
       - `step_count_list`: stores all minimal step count that visited this location. It is useful when we can get the minimum steps to achieve the goal fast.
       - `previous_list`: stores all (previous x, previous y) which are node came from to current location. (the origin come from) It is useful when we trace back from the goal.
       - `step_size_list`: stores all unique step size that visited this loca- tion. It is useful when one of location is required to step twice.

[^4]: In my solution, it only solves the square mazes
