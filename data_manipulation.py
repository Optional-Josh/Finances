import pandas as pd
import json

def dataframes():

    with open('money.json', 'r') as read_file:
        data = json.load(read_file)

    # create a list within the function
    records = []

    # iterates through the list containing dictionaries
    for dict in data:
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
    string_df = df.to_string(index=False)

    # returns the variable to be used outside the function
    return string_df

    