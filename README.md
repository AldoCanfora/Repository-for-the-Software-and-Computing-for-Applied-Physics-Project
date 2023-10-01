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
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be con-
densed into the following:
- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. The first generation is created
by applying the above rules simultaneously to every cell in the seed, live or dead; births
and deaths occur simultaneously, and the discrete moment at which this happens is
sometimes called a tick.
The rules continue to be applied repeatedly to create further generations.

### Emergent forms
As is a property of complex systems, the operation of these rules produces emergent new forms, with properties that are not
predictable from the initial conditions. These new forms and properties do not involve
changes in initial conditions, since the counters are unchanged, but in the emergent
forms, the configurations that emerge, and their properties.

Conway identifies three distinctive emergent forms. 
- “Still life”
- “Blinker”
- “Movers” which include “Gliders”, which move across the grid.

![config](./images/still_life.jpg)

In figure above, an example of a still life. The pattern stabilizes into a fixed form.

![config](./images/other_stable_forms.jpg)

There are also other stable forms such as those shown in the figure above.

![config](./images/blinker.jpg)

In figre above an example of a blinker, which is a pattern that oscillates with a fixed period,
that is, after n iterations the pattern returns to a previously visited state. In the example
this pattern has period 2.

![config](./images/glider.jpg)
The glider is a repeating pattern that travels across the grid. Their movement is diagonal in cellular grid  
and after one period come back to initial pattern and this procedure continues.
Therefore important feature of gliders is their movement in cellular grid. Figure above shows a glider whit period 4. 


## Structure of the project
These are the steps in order to start the program and to plot the results:

First, the user has to choose between the different dimension of the grid (in our case there is only one, [configuration](configuration.txt)) and eventually write a new one, using the syntax of configuration; if the user wants to do so, he has to specify the grid parameters (WIDTH, HEIGHT). The actual grid used in [cellular_automata](cellular_automata.py) is scaled by going to divide both WIDTH and HEIGHT by 10, approximating the result by default to the nearest integer. The minimum selectable values WIDTH and HEIGHT are greater than 20, to have a grid of at least 2 by 2.
Then, to start the Conway's Game of Life algortihm the user has to launch the file [cellular_automata](cellular_automata.py) which imports its parameters from [configuration](configuration.txt). 
Running the file [cellular_automata](cellular_automata.py), with the command entered by the user **"python cellular_automata.py"**, through the pygame library, will display a window where you can see the time evolution of the Conway's Game of Life.

This is how I divided my project into blocks:

- In the file [cellular_automata](cellular_automata.py) I have built the Conway's Game of life functions that initialize the grid, count the number of neighbors in each cell, update the grid state, display the grid state in real time. 

- In the file [testing](testing.py) I have tested all the [cellular_automata](cellular_automata.py) functions to ensure that all of them work properly, using hypothesis testing for the test function about the initialization of the grid. For the other functions to be tested, I used examples of grids on which to make asserts. In addition, I included testing functions for special cases, such as all live cells or all death cells, and emergent forms.

- In the file [configuration](configuration.txt) there are the definitions of the parameters used in the [cellular_automata](cellular_automata.py) e [testing](testing.py), there are definitions of the grid size measurement WIDTH and HEIGHT.




