"""
Sajjan Acharya
11:25, 11th April, 2024 
Understanding Exception Handling in Python 
"""

# Some notes about the basics 
"""
Exceptions: 
    - handle errors appropriately 
    - 
Try/Except:
    - try has code that can produce errors 
    - except has the code to handle the error if it occured 

Multiple Exception: 
    - all exceptions in a tuple
    - exceptions in separate blocks such that exception is handled by one of the blocks if any
    - 
Trapping all Exceptions:
    - no idea abouot exceptions that can be thrown by program 
    - 

Finally: 
    - runs whether an exception occured or not, runs anyway 

    - clean up after a script 

Try/Else: 
    - else -> runs only when no exception occurs 
            - exceptions here won't be caught 

Types of Errors that can occur: 
    - ValueError : 
    - OSError : 
    - ValueError : 
    - RuntimeError : 
    - TypeError : 
    - NameError : 
"""

try:
    file = open('demo.txt', 'rb')
except(IOError, EOFError) as e:
    print('Error error') 

# different blocks for each error 
try:
    file2 = open('demo2.txt', 'wb')
except IOError as e:
    print('error ')
    raise e
except EOFError as e:
    print(e)
    raise e 
except:
    print('Another error')
else: 
    print("This runs if no exception occurs,")
    #no exceptions are handled here
    f = open('demo3.txt', 'rb')
    # -> This gives error and interrupts the flow of the program
    print(f)

finally:
    print("Finally of second exceptional clause")

# trapping all exceptions 
try: 
    file = open('t.txt', 'rb')
except Exception as e:
    # print(e)
    # raise e
    pass
except:
    print('Other errors') 

else: 
    # does not run since exception occurs above 
    print("This runs if no exception occurs,")
finally: 
    print("Finally clause is run here")
