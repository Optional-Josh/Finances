def write_file(content):
    with open('money.txt', 'w') as file:
        file.write(content)

def read_file():
    with open('money.txt', 'r') as read_file:
        print(read_file.read())