from compiler import Compiler
from record import Record
from file_manipulation import write_into_file, read_file


# function that asks for user choices and serves as a main menu
def main_menu():
    while True:
        user_input = input("Type y to enter a record for your finances or q to quit the menu: ")

        if user_input.lower() == "y":
            compiler = Compiler()
            record = Record(compiler.date, compiler.category, compiler.description, compiler.amount)
            record_dict = record.to_dict()
            write_into_file(record_dict)
            read_file()


        elif user_input.lower() == "q":
            break
        else:
            print("Please input from choices given only")

# serves as the main python file, which will run the other python modules
if __name__ == "__main__":
    main_menu()

    