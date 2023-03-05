import pygame
import random
from functools import reduce

# window dimension
WIDTH = 640
HEIGHT = 480

# Initialize pygame and window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create grid of live o dead cels
def create_grid(width, height):
    return [[random.randint(0, 1) for j in range(width)] for i in range(height)]

# to count number of live neighbors
def count_neighbors(grid, x, y):
    neighbors = [grid[(x + i) % len(grid)][(y + j) % len(grid[0])] for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
    return reduce(lambda x, y: x + y, neighbors)

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
grid = create_grid(WIDTH//10, HEIGHT//10)

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
