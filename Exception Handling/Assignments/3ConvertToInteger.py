"""
Write a Python program that takes a user input and converts it to an integer. Handle the ValueError and display a custom error message when the input cannot be converted to an integer.
"""

def convertToInteger():
    try: 
        user_inp = input("Enter a number:")
        int_ = int(user_inp)
        print("Integer is:", int_)
    except ValueError as e:
        print(e)

convertToInteger()