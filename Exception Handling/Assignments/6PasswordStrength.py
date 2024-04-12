"""
Implement a program that reads user input for a password. Create a custom exception WeakPasswordError to handle cases where the password is shorter than 8 characters.

"""
import logging

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('PasswordStrengthChecker.log')
handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

class WeakPasswordError(Exception):
    pass 

def checkPasswordStrength(password):
    try:
        if(len(password))>8:
            print("Good strong password")
            logger.info(f'Strong password with length {len(password)}')
        else:
            logger.error('WeakPasswordError: Too short password, needs to be at least 8 characters!')
            raise WeakPasswordError('Too short password, needs to be at least 8 characters!')
        
    except Exception as e:
        print('Error is', e)

checkPasswordStrength(input("Enter a password:"))