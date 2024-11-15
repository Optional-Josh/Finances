import pandas as pd
import json

# function that reads the contents of a txt file
def get_data_json():
    with open('money.json', 'r') as read_file:
        data = json.load(read_file)

        return data

def dataframes(placeholder):
    # create a list within the function
    records = []

    # iterates through the list containing dictionaries
    for dict in placeholder:
        # iterates through the key value pairs of each dictionary
        for date, dicts in dict.items():
            # iterates through the list containing dictionaries
            for dict in dicts:
                # each dictionary within a list, will become a dictionary in this format
                record = {
                    "date": date,
                    "category": dict["category"],
                    "description": dict["description"],
                    "amount": dict["amount"]
                }
                # adds the formatted dictionary record into local variable records which is a list
                records.append(record)
    # variable that stores a data frame containing the list of dicionaries
    df = pd.DataFrame(records)

    # returns the variable to be used outside the function
    return df

if __name__ == "__main__":
    data = get_data_json()
    test = dataframes(data)
    print(test)
    