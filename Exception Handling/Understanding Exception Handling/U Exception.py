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
import logging 

# for the format of logging
# level denotes the importance or level of severity? 
# Update: Level denotes the level and above it that we want to be logged in the log file 
logging.basicConfig(filename='errors.log', level = logging.INFO)

try:
    file = open('demo.txt', 'rb')
except(IOError, EOFError) as e:
    logging.error('I/O Error: %s', e)
    

# different blocks for each error 
try:
    file2 = open('demo2.txt', 'wb')
except IOError as e:
    logging.error('I/O Error: %s', e)
    raise e
except EOFError as e:
    logging.error('EOF Error: %s', e)
    raise e 
except Exception as e:
    logging.error('Other errors: %s', e)

else: 
    logging.info('No exceptions occured')
    print("This runs if no exception occurs,")
    #no exceptions are handled here
    # f = open('demo3.txt', 'rb')
    # -> This gives error and interrupts the flow of the program
    # print(f)


finally:
    print("Finally of second exceptional clause\n")


# trapping all exceptions 
try: 
    file = open('t.txt', 'rb')
except Exception as e:
    logging.error('Exception: %s',e)
except:
    print('Other errors') 

else: 
    logging.info('No exceptions occured')
    # does not run since exception occurs above 
    print("This runs if no exception occurs,")
finally: 
    print("Finally clause is run here")
