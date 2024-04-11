"""
Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of individuals who are 18 years or older.
"""

def checkAge(csv_file):
    with open(csv_file) as f:
        # 'w' will create the new file if it does not exist 
        with open('new_csv.csv', 'w') as f2:
            for line in f:
                row = line.strip().split(',')

                # checking the age 
                if (int(row[1])>=18):
                    f2.write(f'{row[0]},{row[1]}\n')

checkAge('data.csv')