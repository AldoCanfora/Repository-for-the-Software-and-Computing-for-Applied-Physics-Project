import numpy as np
import pytest
import cellular_automata
import hypothesis
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given

@pytest.fixture
def width():
    return 1000  
@pytest.fixture
def height():
    return 700   

def test_initial_state_grid(width,height):
    #Initialazing the model with width*height spins of values 0 and 1."
    model = cellular_automata.initial_state_grid(height,width) 
    #Test if the dimensions of the grid are width and height."
    assert len(model) == width
    assert len(model[0]) == height
    #Test if all the values have really the values 0 and 1."
    assert ((model == 0) | (model == 1)).all()


'''def test_create_grid():
    grid = create_grid(3, 3)
    assert len(grid) == 3
    assert len(grid[0]) == 3
    assert len(grid[1]) == 3
    assert len(grid[2]) == 3
    for row in grid:
        for cell in row:
            assert cell in (0, 1)'''

'''def test_create_grid():
    width, height = 1000, 700
    grid = create_grid(width, height)
    
    # check grid dimensions
    assert len(grid) == height
    assert len(grid[0]) == width

    # check cell's value: 0 or 1
    for row in grid:
        for cell in row:
            assert cell in (0, 1)

    # check that the grid is indeed a list of lists (matrix nxm)
    assert isinstance(grid, list)
    for row in grid:
        assert isinstance(row, list)'''



'''
import pytest
from main import create_grid

def test_create_grid():
    # Test con dimensioni 0
    assert create_grid(0, 0) == []

    # Test con dimensioni maggiori di 0
    grid = create_grid(3, 3)
    assert len(grid) == 3
    assert len(grid[0]) == 3

    # Test per verificare che la funzione generi solo 0 e 1
    for row in grid:
        for cell in row:
            assert cell in [0, 1]

'''

@pytest.fixture
def grid():
    return [
        [0, 0, 1],
        [1, 1, 0],
        [0, 1, 0]
    ]

def test_count_neighbors_center(grid):
    assert count_neighbors(grid, 1, 1) == 3

def test_count_neighbors_corner(grid):
    assert count_neighbors(grid, 0, 0) == 2

def test_count_neighbors_edge(grid):
    assert count_neighbors(grid, 0, 1) == 3

#def test_count_neighbors_wraparound(grid):
#    assert count_neighbors(grid, 0, 2) == 3
#    assert count_neighbors(grid, 2, 0) == 2
#    assert count_neighbors(grid, 2, 2) == 2


'''def test_count_neighbors_invalid_coords(grid):
    with pytest.raises(IndexError):
        count_neighbors(grid, -1, -1)
    with pytest.raises(IndexError):
        count_neighbors(grid, 3, 3)'''
def test_count_neighbors_invalid_coords(grid):
    with pytest.raises(IndexError):
        count_neighbors(grid, -1, -1)
    with pytest.raises(IndexError):
        count_neighbors(grid, len(grid), len(grid[0]))
    with pytest.raises(IndexError):
        count_neighbors(grid, -1, len(grid[0]))
    with pytest.raises(IndexError):
        count_neighbors(grid, len(grid), -1)


def test_update_cell():
    # Test con una cella morta e 3 celle vive vicine
    grid = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 1

    # Test con una cella viva e 1 cella viva vicina
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 0

    # Test con una cella viva e 2 celle vive vicine
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 1

    # Test con una cella viva e 4 celle vive vicine
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 0

    # Test con una cella morta e 1 cella vive vicine
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 1

    # Test con una cella morta e 3 celle vive vicine
    grid = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 1

    # Test con una cella morta e 4 celle vive vicine
    grid = [
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 0




def test_update_grid():
    # Test con una griglia predefinita
    grid = [[1, 1, 1],
            [0, 0, 0],
            [0, 0, 0]]
    expected = [[1, 0, 1],
                [1, 0, 1],
                [0, 0, 0]]
    assert update_grid(grid) == expected
    
    # Test con una griglia in cui tutte le celle sono morte
    grid = [[0 for _ in range(10)] for _ in range(10)]
    expected = [[0 for _ in range(10)] for _ in range(10)]
    assert update_grid(grid) == expected
    
    # Test con una griglia in cui tutte le celle sono vive
    grid = [[1 for _ in range(10)] for _ in range(10)]
    expected = [[0 for _ in range(10)] for _ in range(10)]
    assert update_grid(grid) == expected
