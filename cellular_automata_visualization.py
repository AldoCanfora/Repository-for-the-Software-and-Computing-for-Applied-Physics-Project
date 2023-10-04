import cellular_automata
import pygame
import parameters

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
