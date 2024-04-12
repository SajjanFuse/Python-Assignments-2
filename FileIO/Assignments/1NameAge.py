"""
Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of individuals who are 18 years or older.
"""
import logging

# Configure logger
logging.basicConfig(filename='nameAge.log', level=logging.DEBUG,
                    format=' %(levelname)s - %(message)s')


def checkAge(csv_file):
    try:
        with open(csv_file) as f:
            # 'w' will create the new file if it does not exist 
            with open('new_csv.csv', 'w') as f2:
                for line in f:
                    row = line.strip().split(',')

                    # checking the age 
                    if (int(row[1])>=18):
                        f2.write(f'{row[0]},{row[1]}\n')

            logging.info('Csv Updated with names of people older than 18')
    except FileNotFoundError as e:
        logging.error("File not found: %s", e)
        
    except IndexError as e:
        logging.error("IndexError: %s", e)
        
    except ValueError as e:
        logging.error("ValueError: %s", e)
        
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        
checkAge('data.csv')
checkAge('nodata.csv')