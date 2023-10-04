import numpy as np
import pygame

# Prompt the user to enter the filename
"""
This script reads a configuration file specified by the user, parses it line by line, 
and stores the configuration values in a dictionary. It assumes that the configuration file contains key-value 
pairs separated by '='. The keys are strings, and the values are expected to be integers.

Usage:
1. Run the script and provide the configuration file's filename when prompted.
2. The script will attempt to open and read the file, extract key-value pairs, 
   and store them in the 'config_values' dictionary.
3. If the specified file is not found, a 'FileNotFoundError' will be raised, and an error message will be displayed.
4. If any other error occurs during file reading or parsing, 
   an error message will be displayed with details about the exception.

Example Configuration File Format:
-------------------
key1=42
key2=123
key3=987
-------------------

Note:
- Ensure that the configuration file is in the specified format, with one key-value pair per line.
- The values are assumed to be integers, so any non-integer values will raise an error.

Author: Aldo Canfora
Date: 04/10/2023
"""
filename = input("Enter configuration filename: ")

config_values = {}
try:
    with open(filename, 'r') as config_file:
        for line in config_file:
            key, value = line.strip().split('=')
            config_values[key] = int(value)
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

WIDTH = config_values.get('WIDTH') 
HEIGHT = config_values.get('HEIGHT')
seed_value = config_values.get('seed_value')

# Initialize pygame and window
#pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create grid of live o dead cels
def initial_state_grid(width, height):
    """
    Generate a random binary grid as the initial state configuration.

    Parameters:
        width (int): The width of the grid.
        height (int): The height of the grid.

    Returns:
        numpy.ndarray: A grid of random binary values (0 or 1) with the specified dimensions.

    Raises:
        ValueError: If either width or height is less than 2.
    """
    if width < 2 or height < 2:
        raise ValueError('Both dimensions of the grid must be >= 2, but are {} and {}'.format(width,height))
    np.random.seed(seed_value)
    init_state_grid = np.random.choice([0, 1],size=(height,width)) 
    return init_state_grid


def count_neighbors(grid, x, y):
    """
    Count the number of alive neighbors for a cell in a binary grid.

    Parameters:
        grid (list): The binary grid representing the current state.
        x (int): The x-coordinate of the cell to count neighbors for.
        y (int): The y-coordinate of the cell to count neighbors for.

    Returns:
        int: The number of alive neighbors (value equal to 1) for the specified cell.

    Note:
        This function counts the number of alive neighbors for a cell in the grid.
        It considers the 8 neighboring cells (top, bottom, left, right, and diagonals).

    Examples:
        Given a binary grid, you can use this function to count the number of alive neighbors for a specific cell.
        alive_neighbors = count_neighbors(binary_grid, x, y)
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # Check if coordinates are valid
    is_valid_coord = lambda i, j: 0 <= i < num_rows and 0 <= j < num_cols

    # Compute value of neighbor if coordinat is valid, otherwise return 0
    get_neighbor_value = lambda i, j: grid[i][j] if is_valid_coord(i, j) else 0

    # Generate a list of neighbors's values
    alive_neighbors = sum(
        get_neighbor_value(x+i, y+j) == 1
        for i in range(-1, 2)
        for j in range(-1, 2)
        if not (i == 0 and j == 0)
    )

    return alive_neighbors



# to update grid according to rules
def update_cell(grid, x, y):
    """
    Update the state of a cell in a binary grid based on Conway's Game of Life rules.

    Parameters:
        grid (numpy.ndarray): The binary grid representing the current state.
        x (int): The x-coordinate of the cell to update.
        y (int): The y-coordinate of the cell to update.

    Returns:
        int: The updated state of the cell (1 for alive, 0 for dead) based on the rules.

    Note:
        This function follows the rules of Conway's Game of Life:
        - If a live cell has 2 or 3 live neighbors, it remains alive; otherwise, it dies.
        - If a dead cell has exactly 3 live neighbors, it becomes alive.

    Examples:
        If grid[x][y] == 1 (live cell) and count_neighbors(grid, x, y) is 2 or 3, the cell remains alive.
        If grid[x][y] == 1 (live cell) and count_neighbors(grid, x, y) is not 2 or 3, the cell dies (returns 0).
        If grid[x][y] == 0 (dead cell) and count_neighbors(grid, x, y) is 3, the cell becomes alive (returns 1).
    """
    count = count_neighbors(grid, x, y)
    if grid[x][y] == 1: # considero le celle vive
        return 1 if count in [2, 3] else 0
    else: # considero le celle morte
        return 1 if count == 3 else 0

def update_grid(grid):
    """
    Update the entire binary grid based on Conway's Game of Life rules.

    Parameters:
        grid (list): The binary grid representing the current state.

    Returns:
        list: A new binary grid representing the updated state based on the rules.

    Note:
        This function applies the rules of Conway's Game of Life to each cell in the input grid
        and generates a new grid as the next state.

    Examples:
        Given an initial grid, you can use this function to obtain the next generation grid.
        updated_grid = update_grid(initial_grid)
    """
    return [[update_cell(grid, i, j) for j in range(len(grid[0]))] for i in range(len(grid))]
