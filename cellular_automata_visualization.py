import cellular_automata
import pygame
import configparser
import sys
from sys import argv
import random

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

    config = configparser.ConfigParser()

    # Set a deafult configuration file name
    default_config_file = 'configuration.txt'
    # Check if a command-line argument for the configuration file name has been provided
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        # If no argument is provided, use the default configuration file name
        config_file = default_config_file

    config.read(config_file)

    # Extract the value of seed_value from the configuration file, if present
    seed_value = config.get('settings', 'seed_value', fallback=None)

    # Check if seed_value is present in the configuration file
    if seed_value is not None:
        seed_value = int(seed_value)
    else:
        # If seed_value is not present, generate a random value
        seed_value = random.randint(1, 1000)

    WIDTH = config.get('settings', 'WIDTH')
    HEIGHT = config.get('settings', 'HEIGHT')
    border_type = config.get('settings', 'border_type')

    WIDTH = int(WIDTH)
    HEIGHT = int(HEIGHT)
    seed_value = int(seed_value)


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
#main part of the code

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



