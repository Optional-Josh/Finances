import time

def current_date():
    print("Format of date (MM-DD-YYYY)")
    get_date = input("Please input the date of this finance log\n")
    if get_date == "":
        get_date = time.strftime("%m-%d-%Y", time.localtime())
        return get_date
    
def money_category():
    while True:
        category = input("Type e for \"expenses\" and i for \"income\"\n")
        if category.lower() == 'e':
            return 'Expenses'
        elif category.lower() == 'i':
            return 'Income'
        else:
            print("You did not select from the choices above")

def get_description():
    while True:
        description = input("Type a description of this money log\n")
        if description.strip():
            return description.capitalize()
        print("Description cannot be empty. Please provide a description")

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