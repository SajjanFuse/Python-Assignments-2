"""
Create a function add_to_json that takes a filename and a dictionary as input. The function should read the JSON data from the file, add the new dictionary to it, and write the updated data back to the same file.

"""
# for json
import json 

def add_to_json(filename, dict_):    
    try:
        # r+ for read and write both? 
        with open(filename, 'r+') as file:
            data = json.load(file)
            print(f'Data before appending is {data}')
            for d in dict_:
                data.append(d)
            print(data)
            # to go to the beginning portion of the json file
            # for copying the new appended data from the top
            file.seek(0)

            json.dump(data, file)
            file.truncate()
    
    except FileNotFoundError as e:
        print(e)
        with open(filename, 'w') as file:
            file.dump(dict_, file)

temp_data =[{
    "name": "Ram",
    "age": 30
},
  {  "name": "Sita",
    "age": 25
  }]
# print(temp_data)

add_to_json('NameAge.json', temp_data)