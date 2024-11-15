import time

class Compiler:
    def __init__(self):
        self.date = None
        self.category = None
        self.description = None
        self.amount = None
        

        # invoking class methods
        self.initiate_get_inputs()

        # function that asks user for date, when entered without any input, it puts in today's date based on your system's local time
    def get_date(self):
        print("Format of date (MM-DD-YYYY)")
        self.date = input("Please input the date of this finance log\n")
        if self.date == "":
            self.date = time.strftime("%m-%d-%Y", time.localtime())
    
    # functions that asks user what category of money record it is, whether income or expense, ensures correct input
    def get_category(self):
        while True:
            self.category = input("Type e for \"expenses\" and i for \"income\"\n")
            if self.category.lower() == 'e':
                self.category = 'Expenses'
                break
            elif self.category.lower() == 'i':
                self.category = 'Income'
                break
            else:
                print("You did not select from the choices above")

    # function that asks user for a description of the money record, ensures spaces or blanks will prompt user again till correct input
    def get_description(self):
        while True:
            self.description = input("Type a description of this money log\n")
            if self.description.strip():
                self.description = self.description.capitalize()
                break
            print("Description cannot be empty. Please provide a description")

    # function that asks user for amount or cost of money record, ensures no negative numbers and empty inputs, repeats until positive number is inputted
    def get_amount(self):
        while True:
            try:
                self.amount = int(input("Type an amount of this money log\n"))
                if self.amount <= 0:
                    print("Please input a real number")
                else:
                    self.amount = self.amount
                    break
            except ValueError:
                print("Please input a number")
            
    # function that runs all user input functions, consolidates it and returns it
    def initiate_get_inputs(self):
        self.get_date()
        self.get_category()
        self.get_description()
        self.get_amount()


    # functions that will gather all user inputted date and compile it to be returned
    def return_data(self):
        return self.date, self.category, self.description, self.amount

# running codes section
if __name__ == "__main__":
    compile = Compiler()
    print(compile.date, compile.category, compile.description, compile.amount)