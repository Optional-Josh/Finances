# function that appends via arguments into a file
def write_into_file(content):
    with open('money.txt', 'a') as file:
        file.write(content)

# functions that reads the contents of a txt file
def read_file():
    with open('money.txt', 'r') as read_file:
        print(read_file.read())