import pytest
import cellular_automata

@pytest.fixture
def width():
    return 1000 

@pytest.fixture
def height():
    return 700  

@pytest.fixture
def seed_value():
    return 1  

def test_initial_state_grid(width,height):
    """
Test the initialization of the cellular automaton grid.

This test function checks whether the cellular automaton grid is properly initialized with the specified dimensions
and contains only values of 0 and 1.

Args:
    width (int): The width of the grid.
    height (int): The height of the grid.

Test Steps:
1. Initializes the cellular automaton grid with the specified dimensions, where all values are either 0 or 1.
2. Checks if the dimensions of the grid match the provided width and height.
3. Verifies that all values in the grid are either 0 or 1.

Raises:
    AssertionError: If any of the test conditions fail.

Example Usage:
    test_initial_state_grid(10, 20)  # Test with a 10x20 grid.
    """
    #Initialazing the model with width*height grid of values 0 and 1."
    model = cellular_automata.initial_state_grid(height,width) 
    #Test if the dimensions of the grid are width and height."
    assert len(model) == width
    assert len(model[0]) == height
    #Test if all the values have really the values 0 and 1."
    assert ((model == 0) | (model == 1)).all()


@pytest.fixture
def grid():
    return [
        [0, 0, 1],
        [1, 1, 0],
        [0, 1, 0]
    ]

def test_count_neighbors_center(grid):
    """
Test the counting of neighbors for a cell at the center of the grid.

This test function verifies that the 'count_neighbors' function correctly counts the number of neighboring cells
for a cell located at the center of the grid.

Args:
    grid (list[list[int]]): A 2D grid representing the cellular automaton.

Test Steps:
1. Calls the 'count_neighbors' function with the provided 'grid', in above grid() function, and coordinates (1, 1) 
   representing the center cell.
2. Asserts that the function returns the expected count of neighbors for the center cell.

Raises:
    AssertionError: If the count of neighbors for the center cell is not equal to the expected count.

Example Usage:
    grid = [
        [0, 0, 1],
        [1, 1, 0],
        [0, 1, 0]
    ]
    test_count_neighbors_center(grid)  # Expected result is 3.
    """
    assert cellular_automata.count_neighbors(grid, 1, 1) == 3

def test_count_neighbors_corner(grid):
    """
Test the counting of neighbors for a cell at the corner of the grid.

This test function verifies that the 'count_neighbors' function correctly counts the number of neighboring cells
for a cell located at the corner of the grid.

Args:
    grid (list[list[int]]): A 2D grid representing the cellular automaton.

Test Steps:
1. Calls the 'count_neighbors' function with the provided 'grid', in above grid() function, and coordinates (0, 0) 
   representing the center cell.
2. Asserts that the function returns the expected count of neighbors for the corner cell.

Raises:
    AssertionError: If the count of neighbors for the corner cell is not equal to the expected count.
    """
    assert cellular_automata.count_neighbors(grid, 0, 0) == 2

def test_count_neighbors_edge(grid):
    """
Test the counting of neighbors for a cell at the edge of the grid.

This test function verifies that the 'count_neighbors' function correctly counts the number of neighboring cells
for a cell located at the edge of the grid.

Args:
    grid (list[list[int]]): A 2D grid representing the cellular automaton.

Test Steps:
1. Calls the 'count_neighbors' function with the provided 'grid', in above grid() function, and coordinates (0, 1) 
   representing the center cell.
2. Asserts that the function returns the expected count of neighbors for the edge cell.

Raises:
    AssertionError: If the count of neighbors for the edge cell is not equal to the expected count.
    """    
    assert cellular_automata.count_neighbors(grid, 0, 1) == 3
    

def test_update_cell_death_to_live():
    """
Test the update of a cell in the cellular automaton grid.

This test function verifies the update of a cell in the grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_cell' function with the provided 'grid' and coordinates (1, 1) to update the center cell.
3. Asserts that the function returns the expected state of the updated cell.

Note:
- In this test case, we test the scenario where a cell is initially dead (0) and has 3 neighboring live cells (1). 
According to the rules of the cellular automaton Conway's game of life, such a cell should become alive (1) in 
the next generation.

Raises:
    AssertionError: If the updated state of the cell is not equal to the expected state.
    """
    # Test 1 death cell and 3 near live cells
    grid = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 1

def test_update_cell_live_to_death():
    """
Test the update of a cell in the cellular automaton grid.

This test function verifies the update of a cell in the grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_cell' function with the provided 'grid' and coordinates (1, 1) to update the center cell.
3. Asserts that the function returns the expected state of the updated cell.

Note:
- In this test case, we test the scenario where a cell is initially live (1) and has no neighbors, so all death cells near(0). 
According to the rules of the cellular automaton Conway's game of life, such a cell should become death (0) in 
the next generation.

Raises:
    AssertionError: If the updated state of the cell is not equal to the expected state.
    """
    # Test 1 live cell and no near live cells
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0

def test_update_cell_live_with_one_neighbor():
    """
Test the update of a cell in the cellular automaton grid.

This test function verifies the update of a cell in the grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_cell' function with the provided 'grid' and coordinates (1, 1) to update the center cell.
3. Asserts that the function returns the expected state of the updated cell.

Note:
- In this test case, we test the scenario where a cell is initially live (1) and has 1 neighbor live cells (1). 
According to the rules of the cellular automaton Conway's game of life, such a cell should become death (0) in 
the next generation.

Raises:
    AssertionError: If the updated state of the cell is not equal to the expected state.
    """
    # Test 1 live cell and 1 near live cell
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0

def test_update_cell_live_with_4_neighbors():
    """
Test the update of a cell in the cellular automaton grid.

This test function verifies the update of a cell in the grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_cell' function with the provided 'grid' and coordinates (1, 1) to update the center cell.
3. Asserts that the function returns the expected state of the updated cell.

Note:
- In this test case, we test the scenario where a cell is initially live (1) and has 4 neighboring live cells (1). 
According to the rules of the cellular automaton Conway's game of life, such a cell should become death (0) in 
the next generation.

Raises:
    AssertionError: If the updated state of the cell is not equal to the expected state.
    """
    # Test 1 live cell and 4 near live cells
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0


def test_update_cell_live_with_2_neighbors():
    """
Test the update of a cell in the cellular automaton grid.

This test function verifies the update of a cell in the grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_cell' function with the provided 'grid' and coordinates (1, 1) to update the center cell.
3. Asserts that the function returns the expected state of the updated cell.

Note:
- In this test case, we test the scenario where a cell is initially live (1) and has 2 neighboring live cells (1). 
According to the rules of the cellular automaton Conway's game of life, such a cell should stay alive (1) in 
the next generation.

Raises:
    AssertionError: If the updated state of the cell is not equal to the expected state.
    """
    # Test 1 live cell and 2 near live cells
    grid = [
        [0, 1, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 1

def test_update_cell_death_with_4_neighbors():
    """
Test the update of a cell in the cellular automaton grid.

This test function verifies the update of a cell in the grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_cell' function with the provided 'grid' and coordinates (1, 1) to update the center cell.
3. Asserts that the function returns the expected state of the updated cell.

Note:
- In this test case, we test the scenario where a cell is initially dead (0) and has 4 neighboring live cells (1). 
According to the rules of the cellular automaton Conway's game of life, such a cell should stay death (0) in 
the next generation.

Raises:
    AssertionError: If the updated state of the cell is not equal to the expected state.
    """
    # Test 1 death cell with 4 near live cells
    grid = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0

def test_update_cell_death_with_3_neighbors():
    """
Test the update of a cell in the cellular automaton grid.

This test function verifies the update of a cell in the grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_cell' function with the provided 'grid' and coordinates (1, 1) to update the center cell.
3. Asserts that the function returns the expected state of the updated cell.

Note:
- In this test case, we test the scenario where a cell is initially dead (0) and has 3 neighboring live cells (1). 
According to the rules of the cellular automaton Conway's game of life, such a cell should become alive (1) in 
the next generation. This is the same case of test_update_cell_death_to_live but with a different order of neighbors.

Raises:
    AssertionError: If the updated state of the cell is not equal to the expected state.
    """
    # Test 1 death cell with 3 near live cells
    grid = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 1




def test_update_grid():
    """
Test the update of the entire cellular automaton grid.

This test function verifies the update of the entire grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_grid' function with the provided 'grid' to update the entire grid.
3. Asserts that the function returns the expected updated grid.

Note:
- In this test case, we test the update of a predefined grid where live (1) and dead (0) cells are arranged in a 
  specific pattern shown in grid, cell (0,0) beacame alive, cell (0,1) stay alive, cell (0,0) and (0,2) became death, and
  other cells stay death.
- The 'expected' grid represents the state of the grid after one update cycle based on the rules of the cellular automaton.

Raises:
    AssertionError: If the updated grid is not equal to the expected updated grid.
    """
    # Test with a predefined grid
    grid = [[1, 1, 1],
            [0, 0, 0],
            [0, 0, 0]]
    expected = [[0, 1, 0],
                [0, 1, 0],
                [0, 0, 0]]
    
    assert cellular_automata.update_grid(grid) == expected
    
def test_update_grid_all_death():
    """
Test the update of the entire cellular automaton grid.

This test function verifies the update of the entire grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_grid' function with the provided 'grid' to update the entire grid.
3. Asserts that the function returns the expected updated grid.

Note:
- In this test case, we test the update of a predefined grid where all cells are death (0). 
- The 'expected' grid represents the state of the grid after one update cycle based on the rules of the cellular automaton.

Raises:
    AssertionError: If the updated grid is not equal to the expected updated grid.
    """
    # Test with all death cells grid
    grid = [[0 for _ in range(10)] for _ in range(10)]
    expected = [[0 for _ in range(10)] for _ in range(10)]
    assert cellular_automata.update_grid(grid) == expected
    
def test_update_grid_all_live():
    """
Test the update of the entire cellular automaton grid.

This test function verifies the update of the entire grid based on the rules of the cellular automaton Conway's game of life.

Test Steps:
1. Initializes a grid with specific values, where 1 represents a live cell, and 0 represents a dead cell.
2. Calls the 'update_grid' function with the provided 'grid' to update the entire grid.
3. Asserts that the function returns the expected updated grid.

Note:
- In this test case, we test the update of a predefined grid where all cells are alive (1). 
- The 'expected' grid represents the state of the grid after one update cycle based on the rules of the cellular automaton.

Raises:
    AssertionError: If the updated grid is not equal to the expected updated grid.
    """
    # Test with all live cells grid
    grid = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    expected = [[1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]]
    assert cellular_automata.update_grid(grid) == expected


def test_still_life_square_form():
    # Test still life emergent form with square shape
    grid = [[0, 0, 0],
            [0, 1, 1],
            [0, 1, 1]]
    expected = [[0, 0, 0],
                [0, 1, 1],
                [0, 1, 1]]
    assert cellular_automata.update_grid(grid) == expected
    assert cellular_automata.update_grid(expected) == grid


def test_blinker():
    # Test blinker emergent form with switch cross shape
    state_0 = [[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]
    state_1 = [[0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]]
    assert cellular_automata.update_grid(state_0) == state_1
    assert cellular_automata.update_grid(state_1) == state_0



def test_boat():
    # Test boat emergent form
    grid = [[1, 1, 0],
            [1, 0, 1],
            [0, 1, 0]]
    expected = [[1, 1, 0],
                [1, 0, 1],
                [0, 1, 0]]
    assert cellular_automata.update_grid(grid) == expected
    assert cellular_automata.update_grid(expected) == grid


def test_beehive():
    # Test beehive emergent form
    grid = [[0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]]
    expected = [[0, 1, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 1, 0]]
    assert cellular_automata.update_grid(grid) == expected
    assert cellular_automata.update_grid(expected) == grid


def test_loaf():
    # Test loaf emergent form
    grid = [[0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 0]]
    expected = [[0, 1, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 0, 1],
                [0, 0, 1, 0]]
    assert cellular_automata.update_grid(grid) == expected
    assert cellular_automata.update_grid(expected) == grid


def test_glider():
    # Test glider emergent form
    state_0 = [[0, 1, 0, 0],
                [0, 0, 1, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0]]
    state_1 = [[0, 0, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0]]
    state_2 = [[0, 0, 0, 0],
                [0, 0, 1, 0],
                [1, 0, 1, 0],
                [0, 1, 1, 0]]
    state_3 = [[0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 1, 1, 0]]
    state_4 = [[0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 1, 1, 1]]
    assert cellular_automata.update_grid(state_0) == state_1
    assert cellular_automata.update_grid(state_1) == state_2
    assert cellular_automata.update_grid(state_2) == state_3
    assert cellular_automata.update_grid(state_3) == state_4