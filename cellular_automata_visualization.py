import cellular_automata
import pygame

# create initial grid
grid = cellular_automata.initial_state_grid(cellular_automata.WIDTH//10, cellular_automata.HEIGHT//10)

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
            pygame.draw.rect(cellular_automata.screen, color, (j*10, i*10, 10, 10))

    # update grid
    grid = cellular_automata.update_grid(grid)

    # update screen
    pygame.display.update()

# clean and quit pygame
pygame.quit()
