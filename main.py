from details import current_date, money_category, get_description, get_amount

if __name__ == "__main__":
    date = current_date()
    money = money_category()
    description = get_description()
    amount = f"{get_amount()} Pesos"

    while True:
        user_input = input("Type y to enter: ")
        if user_input.lower() == "y":
            print(f"{date} - {money} - {description} - {amount}")
            break
        else:
            print("Please type 'Y'")