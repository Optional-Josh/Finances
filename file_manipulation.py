import json

# function that appends via arguments into a file
def write_into_file(content):
    with open('money.json', 'a') as file:
        json.dump(content, file, indent=2)

# function that reads the contents of a txt file
def read_file():
    with open('money.json', 'r') as read_file:
        data = json.load(read_file)
        formatted_data = (json.dumps(data, indent=2))
    return formatted_data

# function that reads all contents of json, gathers and compiles it
# then its parameters will be the compiled records which will be compiled with any existing data
# lastly, it is written into the json file
def append_dict_to_json(dict):
    try:
        with open("money.json", "r") as actual_file:
            # If json file has data inside, load it into a list
            data = json.load(actual_file)
            if not isinstance(data, list):
                # if existing data is not a list, convert it into a list
                data = [data]
    except (FileNotFoundError, json.JSONDecodeError):
        # if the file does not exist or empty, initialize it with an empty list
        data = []

    data.append(dict)

    # write updated list back to file
    with open("money.json", "w") as actual_file:
        json.dump(data, actual_file, indent=2)