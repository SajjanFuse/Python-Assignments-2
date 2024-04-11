"""
Write a Python program that takes user input for age. Create a custom exception InvalidAgeError to handle cases where the age is below 0 or above 120.
"""
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
            print("Age is validated")

    except ValueError as e:
        print(e)
        print("Is the Value Error")
    except InvalidAgeError as e:
        print("Error occured as ", e)

validateAge(input("Enter any age"))
