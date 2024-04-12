"""
Write a Python program that takes a user input and converts it to an integer. Handle the ValueError and display a custom error message when the input cannot be converted to an integer.
"""

import logging

# Configure logger
logging.basicConfig(filename='integerconverter.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def convertToInteger():
    try: 
        user_inp = input("Enter a number:")
        int_ = int(user_inp)
        print("Integer is:", int_)
    except ValueError as e:
        logging.error('Occured an error converting input to integer: %s', e)

convertToInteger()