import numpy as np

# create grid of live o dead cels
def initial_state_grid(width, height, seed_value):
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


def count_neighbors(grid, x, y, border_type):#MODIFICA DOCSTIRNG AGGIUNGENDO I VARI PARAMETRI E IL RAISE VALUE
    """    
Counts the number of alive neighbors of a cell in a 2D grid based on the specified border type for Conway's game of life.

Args:
    grid (list of list): A 2D grid represented as a list of lists where 1 represents an alive cell and 0 represents a dead cell.
    x (int): The row index of the cell for which neighbors are to be counted.
    y (int): The column index of the cell for which neighbors are to be counted.
    border_type (str): A string indicating the border type to consider for counting neighbors.
        - 'death': Count only cells within the grid boundaries as alive neighbors.
        - 'alive': Treat cells outside the grid boundaries as alive neighbors.
        - 'reflective': Consider neighbors in a reflective manner, mirroring at the grid edges.
        - 'toroidal': Wrap around the grid to count neighbors.

Returns:
    int: The count of alive neighbors based on the specified border type.

Raises:
    ValueError: If the `border_type` is not one of the valid options ('death', 'alive', 'reflective', 'toroidal').
"""
     
    if border_type not in ['death', 'alive', 'reflective', 'toroidal']:
        raise ValueError("border_type must to be set as: death, alive, reflective or toroidal")    
    
    num_rows = len(grid)
    num_cols = len(grid[0])
 
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    alive_neighbors = 0

    for dx, dy in neighbor_offsets:
        if border_type == 'death':
            neighbor_x = x + dx
            neighbor_y = y + dy
            if 0 <= neighbor_x < num_rows and 0 <= neighbor_y < num_cols:
                if grid[neighbor_x][neighbor_y] == 1:
                    alive_neighbors += 1
    
        elif border_type == 'alive':
            neighbor_x = x + dx
            neighbor_y = y + dy
            # If the neighbor is al out of the grid, consider it as alive(1)
            if not (0 <= neighbor_x < num_rows) or not (0 <= neighbor_y < num_cols):
                alive_neighbors += 1
            elif grid[neighbor_x][neighbor_y] == 1:
                alive_neighbors += 1

        
        elif border_type == 'reflective':
            neighbor_x = x + dx
            neighbor_y = y + dy

            # Implementation reflective borders
            if neighbor_x < 0:
                neighbor_x = -neighbor_x - 1
            elif neighbor_x >= num_rows:
                neighbor_x = num_rows - 1

            if neighbor_y < 0:
                neighbor_y = -neighbor_y - 1
            elif neighbor_y >= num_cols:
                neighbor_y = num_cols - 1

            if grid[neighbor_x][neighbor_y] == 1:
                alive_neighbors += 1


        elif border_type == 'toroidal':
            neighbor_x = (x + dx) % num_rows
            neighbor_y = (y + dy) % num_cols
            if grid[neighbor_x][neighbor_y] == 1:
                alive_neighbors += 1

    return alive_neighbors


# to update grid according to rules
def update_cell(grid, x, y, border_type):
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
    count = count_neighbors(grid, x, y, border_type)
    if grid[x][y] == 1: # considering live cells
        return 1 if count in [2, 3] else 0
    else: # considering death cells
        return 1 if count == 3 else 0

def update_grid(grid, border_type):
    """
    Update the entire binary grid based on Conway's Game of Life rules with death borders.

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
    #return [[update_cell(grid, i, j, border_type) for j in range(len(grid[0]))] for i in range(len(grid))]
    shape = grid.shape

    # Define a vectorized version of update_cell to apply to each element in the grid
    vectorized_update_cell = np.vectorize(lambda i, j: update_cell(grid, i, j, border_type))

    # Create an updated grid by applying vectorized_update_cell to each pair of indices
    updated_grid = np.fromfunction(vectorized_update_cell, shape, dtype=np.int8)

    return updated_grid

