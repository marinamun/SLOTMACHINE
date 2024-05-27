def deposit():
    while True:
        amount = input("Insert coins: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number")
        else:
            print("Please enter a positive number")
    
    return amount