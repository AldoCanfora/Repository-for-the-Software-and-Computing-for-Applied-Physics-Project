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