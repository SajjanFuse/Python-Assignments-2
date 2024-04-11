"""
Create a function search_log that takes a log file and a search keyword as input. The function should find and display all lines containing the search keyword.
"""
def search_log(logfile, keyword):
    output_list = []
    try: 
        with open(logfile, 'r') as file:
            # for line number 
            index = 0
            for f in file:
                # in this case, - is used to separate columns in logfile
                # for including all lowercase or uppercase together
                if keyword.lower() in f.lower():
                    output_list.append(f'Line no: {index}, Line: "{f}"')
                index+=1

    except FileNotFoundError as e :
        print("File is not found")
        print(e)
    if len(output_list)==0:
        print('No matches found')
    return output_list

all_results = search_log('logfile.txt', input("Enter the keyword to search: "))

for res in all_results:
    print(res)

