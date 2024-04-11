"""
Write a Python program that takes two integers as input and performs division (num1 / num2). Handle the ZeroDivisionError and display a custom error message when the second number is zero
"""

def getDivision(num1, num2):
    res = 0 
    try: 
        res = num1/num2 
    except ZeroDivisionError as e:
        print('The second number cannot be zero') 
        
        # this will result in the halt of the program 
        # without raise, only error is seen and program keeps running
        raise e
    except: 
        print("Any other errors have occured")

    return res 

print(getDivision(3,5))

print(getDivision(0,4))

# this gives the custom error message for second number being zero
print(getDivision(9,0))

print(getDivision(45,2))