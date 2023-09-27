import numpy as np
import pytest
import cellular_automata
import hypothesis
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given

# Read WIDTH and HEIGHT value from configuration.txt file
config_values = {}
with open('configuration.txt', 'r') as config_file:
    for line in config_file:
        key, value = line.strip().split('=')
        config_values[key] = int(value)



@given(width=st.integers(2, config_values['WIDTH']), height=st.integers(2, config_values['HEIGHT']))    
def test_initial_state_grid(width,height):
    #Initialazing the model with width*height spins of values 0 and 1."
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
    assert cellular_automata.count_neighbors(grid, 1, 1) == 3

def test_count_neighbors_corner(grid):
    assert cellular_automata.count_neighbors(grid, 0, 0) == 2

def test_count_neighbors_edge(grid):
    assert cellular_automata.count_neighbors(grid, 0, 1) == 3

#def test_count_neighbors_wraparound(grid):
#    assert count_neighbors(grid, 0, 2) == 3
#    assert count_neighbors(grid, 2, 0) == 2
#    assert count_neighbors(grid, 2, 2) == 2


'''def test_count_neighbors_invalid_coords(grid):
    with pytest.raises(IndexError):
        count_neighbors(grid, -1, -1)
    with pytest.raises(IndexError):
        count_neighbors(grid, 3, 3)'''
'''def test_count_neighbors_invalid_coords(grid):
    with pytest.raises(IndexError):
        cellular_automata.count_neighbors(grid, -1, -1)
    with pytest.raises(IndexError):
        cellular_automata.count_neighbors(grid, len(grid), len(grid[0]))
    with pytest.raises(IndexError):
        cellular_automata.count_neighbors(grid, -1, len(grid[0]))
    with pytest.raises(IndexError):
        cellular_automata.count_neighbors(grid, len(grid), -1)'''


def test_update_cell():
    # Test 1 death cell and 3 near live cells
    grid = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 1

    # Test 1 live cell and no near live cells
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0

    # Test 1 live cell and 1 near live cell
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0

    # Test 1 live cell and 4 near live cells
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0

    # Test 1 live cell and 2 near live cells
    grid = [
        [0, 1, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 1

    # Test 1 death cell with 4 near live cells
    grid = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 0

    # Test 1 death cell with 3 near live cells
    grid = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert cellular_automata.update_cell(grid, 1, 1) == 1




def test_update_grid():
    # Test with a predefined grid
    grid = [[1, 1, 1],
            [0, 0, 0],
            [0, 0, 0]]
    expected = [[0, 1, 0],
                [0, 1, 0],
                [0, 0, 0]]
    
    assert cellular_automata.update_grid(grid) == expected
    
def test_update_grid_all_death():
    # Test with all death cells grid
    grid = [[0 for _ in range(10)] for _ in range(10)]
    expected = [[0 for _ in range(10)] for _ in range(10)]
    assert cellular_automata.update_grid(grid) == expected
    
def test_update_grid_all_live():
    # Test with all live cells grid
    grid = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    expected = [[1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]]
    assert cellular_automata.update_grid(grid) == expected
