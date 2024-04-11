"""
Write a Python program that takes two integers as input and performs division (num1 / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and display appropriate error messages.
"""

def getDivision(num1, num2):
    res = 0 
    try:  
        res = int(num1)/int(num2) 
        print(res)
    except ZeroDivisionError as e:
        print('The second number cannot be zero') 
        
        # this will result in the halt of the program 
        # without raise, only error is seen and program keeps running
        # raise e
        print(e)
    except ValueError as e:
        print("value error is occured as:")
        print(e)

    except Exception as e:
        print("Any other errors have occured")
        print(e)

    return res 

num1 = input("Enter first number")
num2 = input("Enter second number")
getDivision(num1, num2)