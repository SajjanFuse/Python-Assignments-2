"""
Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. Handle the FileNotFoundError and display an error message if the file is not found.
"""

import logging

# Configure logger
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def readFile(filename):
    try: 
        file = open(filename, mode='rb')
        for line in file:
            print(line)
    except FileNotFoundError as e:
        logging.error('File %s not found: %s', filename, e)
    finally:
        logging.info("File operation completed for %s", filename)

readFile('demo.txt')

readFile('random.txt')
