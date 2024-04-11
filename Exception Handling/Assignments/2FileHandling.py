"""
Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. Handle the FileNotFoundError and display an error message if the file is not found.
"""

def readFile(filename):
    try: 
        file = open(filename,mode='rb')
        for line in file:
            print(line)
    except FileNotFoundError as e:
        print('File is not found')
        print(e) 
    finally:
        print("Thus, file is either read or error is displayed")

readFile('demo.txt')

readFile('random.txt')
