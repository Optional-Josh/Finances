from user_inputs import User_Inputs
from record import Record
from file_manipulation import read_file, append_dict_to_json
import time



# function that asks for user choices and serves as a main menu
def main_menu():
    while True:
        user_input = input("Type y to enter a record for your finances or q to quit the menu: ")

        if user_input.lower() == "y":
            # use class that gathers and validates user input
            compiler = User_Inputs()

            # another variable to store gathered inputs into another class which compiles it
            record = Record(compiler.date, compiler.category, compiler.description, compiler.amount)
            record_dict = record.to_dict() # class method that returns a dictionary object
            
            # function that deals will append the data into json file
            append_dict_to_json(record_dict)
            print("Your inputs have been saved into the json file")

            # delay final execution for added effect
            time.sleep(3)

            # function to read contents of json
            read_file()


        elif user_input.lower() == "q":
            break
        else:
            print("Please input from choices given only")

# serves as the main python file, which will run the other python modules
if __name__ == "__main__":
    main_menu()

    