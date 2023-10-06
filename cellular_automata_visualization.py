import cellular_automata
import pygame

# Prompt the user to enter the filename
if __name__ == "__main__":
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
                config_values[key] = value
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    WIDTH = int(config_values.get('WIDTH'))
    HEIGHT = int(config_values.get('HEIGHT'))
    seed_value = int(config_values.get('seed_value'))
    border_type = config_values.get('border_type')



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
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create initial grid
grid = cellular_automata.initial_state_grid(WIDTH//10, HEIGHT//10, seed_value)

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
    grid = cellular_automata.update_grid(grid, border_type)

    # update screen
    pygame.display.update()

# clean and quit pygame
pygame.quit()



