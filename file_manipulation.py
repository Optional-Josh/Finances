import json

# function that appends via arguments into a file
def write_into_file(content):
    with open('money.json', 'a') as file:
        json.dump(content, file, indent=2)

# functions that reads the contents of a txt file
def read_file():
    with open('money.json', 'r') as read_file:
        data = json.load(read_file)
        print(data)