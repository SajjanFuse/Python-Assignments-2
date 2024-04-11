"""
Sajjan Acharya
13:33, 11th April, 2024
Understanding IO and File Handling in Python
"""

# Basic Notes about I/O of Files in Python 

"""
Opening a file: 
    - to write or read 
    - a : append
    - w : write
With:
    - to automate closing of a file 
    - readLines() to read all lines in a file 
    - rStrip() to remove extraneous line break at end of each line

csv: 
    - comma separated values 
    - rstrip() to remove new line feature
    - split(',') to split into 2 or more items separated by comma

Binary Files and PIL:
    - Binary : collection of 1s and 0s 
    - store anything 
    PIL
        - image files 
        - 
"""

# Rest are easy 
# CSV 

with open('demo_csv.csv') as csv_file:
    for line in csv_file:
        each_row = line.strip().split(',')
        print(each_row[0], "\t", each_row[-1])

