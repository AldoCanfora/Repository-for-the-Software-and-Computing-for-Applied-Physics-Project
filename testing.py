#import pytest
from cellular_automata import create_grid
from cellular_automata import count_neighbors
from cellular_automata import update_cell
from cellular_automata import update_grid


def test_create_grid():
    grid = create_grid(3, 3)
    assert len(grid) == 3
    assert len(grid[0]) == 3
    assert len(grid[1]) == 3
    assert len(grid[2]) == 3
    for row in grid:
        for cell in row:
            assert cell in (0, 1)

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



def test_count_neighbors():
    grid = [
        [1, 1, 0],
        [0, 0, 1],
        [0, 1, 0]
    ]
    assert count_neighbors(grid, 0, 0) == 2
    assert count_neighbors(grid, 0, 1) == 3
    assert count_neighbors(grid, 0, 2) == 2
    assert count_neighbors(grid, 1, 0) == 3
    assert count_neighbors(grid, 1, 1) == 3
    assert count_neighbors(grid, 1, 2) == 2
    assert count_neighbors(grid, 2, 0) == 2
    assert count_neighbors(grid, 2, 1) == 3
    assert count_neighbors(grid, 2, 2) == 1

'''
import pytest
from main import count_neighbors

def test_count_neighbors():
    grid = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    assert count_neighbors(grid, 0, 0) == 2
    assert count_neighbors(grid, 0, 1) == 3
    assert count_neighbors(grid, 1, 1) == 4
    assert count_neighbors(grid, 2, 2) == 2

'''



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

    # Test con una cella morta e 2 celle vive vicine
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert update_cell(grid, 1, 1) == 0

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
