"""
Write a Python program that takes user input for age. Create a custom exception InvalidAgeError to handle cases where the age is below 0 or above 120.
"""

import logging

# Configure logger
logging.basicConfig(filename='AgeProgram.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class InvalidAgeError(Exception):
    pass 


def validateAge(age):
    try:
        age = int(age)
        if (age>120):
            # print("Age cannot be higher than 120")
            raise InvalidAgeError('Higher than 120')
        elif (age<0):
            # print("Age cannot be less than 0")
            raise InvalidAgeError('Less than 0')
        else:
            logging.info("Age is validated")
            

    except ValueError as e:
        logging.error("ValueError occurred: %s", e)
    except InvalidAgeError as e:
        logging.error("InvalidAgeError occurred: %s", e)

validateAge(input("Enter any age"))
