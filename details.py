import time
from file_manipulation import write_into_file, read_file

# function that asks user for date, when entered without any input, it puts in today's date based on your system's local time
def current_date():
    print("Format of date (MM-DD-YYYY)")
    get_date = input("Please input the date of this finance log\n")
    if get_date == "":
        get_date = time.strftime("%m-%d-%Y", time.localtime())
        return get_date
    
# functions that asks user what category of money record it is, whether income or expense, ensures correct input
def category():
    while True:
        category = input("Type e for \"expenses\" and i for \"income\"\n")
        if category.lower() == 'e':
            return 'Expenses'
        elif category.lower() == 'i':
            return 'Income'
        else:
            print("You did not select from the choices above")

# function that asks user for a description of the money record, ensures spaces or blanks will prompt user again till correct input
def get_description():
    while True:
        description = input("Type a description of this money log\n")
        if description.strip():
            return description.capitalize()
        print("Description cannot be empty. Please provide a description")

# function that asks user for amount or cost of money record, ensures no negative numbers and empty inputs, repeats until positive number is inputted
def get_amount():
    while True:
        try:
            amount = int(input("Type an amount of this money log\n"))
            if amount <= 0:
                print("Please input a real number")
            else:
                return amount
        except ValueError:
            print("Please input a number")

# function that runs all user input functions, consolidates it and returns it
def record_log():
    date = current_date()
    money_category = category()
    description = get_description()
    amount = get_amount()

    return f"{date} - {money_category} - {description} - {amount}\n"

# function that asks for user choices and serves as a main menu
def main_menu():
    while True:
        user_input = input("Type y to enter a record for your finances or q to quit the menu: ")
        if user_input.lower() == "y":
            record = record_log()
            write_into_file(record)
            read_file()
        elif user_input.lower() == "q":
            break
        else:
            print("Please input from choices given only")