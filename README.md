# Repository-for-the-Software-and-Computing-for-Applied-Physics-Project

## Cellular Automaton
A cellular automaton is a discrete model of computation studied in automata theory. 
Cellular automata have found application in various areas, including physics, theoretical
biology and microstructure modeling.
A cellular automaton consists of a regular grid of cells, each in one of a finite number
of states, such as on and off. The grid can be in any finite number of dimensions.
For each cell, a set of cells called its neighborhood, is defined relative to the specified
cell. An initial state (time t = 0) is selected by assigning a state for each cell. A
new generation is created (advancing t by 1), according to some fixed rule (generally,
a mathematical function) that determines the new state of each cell in terms of the
current state of the cell and the states of the cells in its neighborhood. The
rule for updating the state of cells is the same for each cell and does not change over
time, and is applied to the whole grid simultaneously.

![config](./images/neighbors_image.jpg)

In the above figure, this cellular automaton is a grid composed by 25 cells. The set of neighbor-
hood is called Moore Neighborhood and it is defined on a two-dimensional square lattice
and it is composed of a central cell and the eight cells that surround it, here indicated
with initials of cardinal points.

 ## Conway’s Game of Life
The Game of Life, also known simply as Life, is a cellular automaton devised by the
British mathematician John Horton Conway in 1970. It is a zero-player game,
meaning that its evolution is determined by its initial state, requiring no further input.
One interacts with the Game of Life by creating an initial configuration and observing
how it evolves. It is Turing complete and can simulate a universal constructor or any
other Turing machine. The universe of the Game of Life is an infinite, two-dimensional
orthogonal grid of square cells, each of which is in one of two possible states, live or
dead (or populated and unpopulated, respectively). Every cell interacts with its eight
neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by repro-
duction.
 

