"""
Implement a program that reads user input for a password. Create a custom exception WeakPasswordError to handle cases where the password is shorter than 8 characters.

"""
class WeakPasswordError(Exception):
    pass 

def checkPasswordStrength(password):
    try:
        if(len(password))>8:
            print("Good strong password")

        else:
            print("ops")
            raise WeakPasswordError('Too short password, needs to be at least 8 characters!')
        
    except Exception as e:
        print('Error is', e)

checkPasswordStrength(input("Enter a password:"))