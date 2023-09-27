import numpy as np
import pygame

# window dimension
WIDTH = 1000
HEIGHT = 700

# Initialize pygame and window
#pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create grid of live o dead cels
def initial_state_grid(width, height):
    if width < 2 or height < 2:
        raise ValueError('Both dimensions of the grid must be >= 2, but are {} and {}'.format(width,height))
    np.random.seed(1)
    init_state_grid = np.random.choice([0, 1],size=(height,width)) 
    return init_state_grid


def count_neighbors(grid, x, y):
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # Check if coordinates are valid
    is_valid_coord = lambda i, j: 0 <= i < num_rows and 0 <= j < num_cols

    # Compute value of neighbor if coordinat is valid, otherwise return 0
    get_neighbor_value = lambda i, j: grid[i][j] if is_valid_coord(i, j) else 0

    # Generate a list of neighbors's values
    neighbor_values = [
        get_neighbor_value(x+i, y+j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if not (i == 0 and j == 0)
    ]

    # Use filter e sum to count alive neighbors
    return sum(filter(lambda v: v == 1, neighbor_values))



# to update grid according to rules
def update_cell(grid, x, y):
    count = count_neighbors(grid, x, y)
    if grid[x][y] == 1: # considero le celle vive
        return 1 if count in [2, 3] else 0
    else: # considero le celle morte
        return 1 if count == 3 else 0

def update_grid(grid):
    return [[update_cell(grid, i, j) for j in range(len(grid[0]))] for i in range(len(grid))]

# create initial grid
grid = initial_state_grid(WIDTH//10, HEIGHT//10)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = (255, 255, 255) if cell == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j*10, i*10, 10, 10))

    # update grid
    grid = update_grid(grid)

    # update screen
    pygame.display.update()

# clean and quit pygame
pygame.quit()
