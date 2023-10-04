import cellular_automata
import pygame
import parameters

"""
This script demonstrates a simple cellular automaton simulation using pygame for visualization.

It initializes a pygame window and creates an initial grid for the cellular automaton. The game loop allows you to 
visualize the automaton's evolution as it updates the grid and displays it on the screen.

Usage:
1. Make sure you have the 'cellular_automata', 'pygame', and 'parameters' modules imported or defined.
2. Run the script, and a pygame window will open with the cellular automaton simulation.
3. You can close the window by clicking the close button.

Requirements:
- pygame: You need to have pygame installed to run this script.
"""

# Initialize pygame and window
screen = pygame.display.set_mode((parameters.WIDTH, parameters.HEIGHT))

# create initial grid
grid = cellular_automata.initial_state_grid(parameters.WIDTH//10, parameters.HEIGHT//10)

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
    grid = cellular_automata.update_grid(grid)

    # update screen
    pygame.display.update()

# clean and quit pygame
pygame.quit()
