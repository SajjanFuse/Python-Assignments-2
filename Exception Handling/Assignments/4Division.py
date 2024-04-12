"""
Write a Python program that takes two integers as input and performs division (num1 / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and display appropriate error messages.
"""

import logging

# Configure logger
logging.basicConfig(filename='division.log', level=logging.DEBUG,
                    format='%(levelname)s - %(message)s')

def getDivision(num1, num2):
    res = 0 
    try:  
        res = int(num1) / int(num2) 
        print(res)
    except ZeroDivisionError as e:
        logging.error('ZeroDivisionError occurred: %s', e)
        
    except ValueError as e:
        logging.error('ValueError occurred: %s', e)
        
    except Exception as e:
        logging.error('An unexpected error occurred: %s', e)
    
    return res 

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
getDivision(num1, num2)
