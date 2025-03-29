import pandas as pd
import matplotlib.pyplot as plt
import json
from collections import defaultdict

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

def graph_data():
    with open('money.json', 'r') as read_file:
        data = json.load(read_file)

    # create a list within the function
    records = []

    # aggregate data
    totals = defaultdict(lambda: {"Income": 0, "Expenses": 0})


    # iterates through the list containing dictionaries
    for entry in data:
        # iterates through the key value pairs of each dictionary
        for date, dicts in entry.items():
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

    # convert date to datetime for proper plotting
    df["date"] = pd.to_datetime(df["date"])

    # separate data into Income and Expenses for plotting
    income_df = df[df["category"] == "Income"].groupby("date").sum().reset_index()
    expenses_df = df[df["category"] == "Expenses"].groupby("date").sum().reset_index()

    # plotting
    plt.figure(figsize=(10,6))

    # Income line
    plt.plot(
        income_df["date"], income_df["amount"], marker="o", label="Income", color="green"
    )

    # Expenses line
    plt.plot(
        expenses_df["date"], expenses_df["amount"], marker="o", label="Expenses", color="red"
    )

    # Customization
    plt.title("Income and Expenses Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12, labelpad=10)
    plt.ylabel("Amount", fontsize=12)
    plt.xticks(rotation=45) # rotate x-tick labels for readability
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Adjust layout to fit labels
    plt.tight_layout()

    # show plot
    plt.show()

