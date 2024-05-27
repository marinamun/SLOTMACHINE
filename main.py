MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COL = 3


symbol_count = {
    "🦀": 2,
    "🥕": 4, 
    "🌻": 6,
    "💧": 8
}


def get_slot_machine_spin(row, column, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    
def deposit():
    while True:
        balance = input("Insert coins: ")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("Please enter a number")
        else:
            print("Please enter a positive number")
    
    return balance


def get_number_of_lines():
    while True:
        lines = input("On how many lines you want to bet? From 1 to " + str(MAX_LINES) + ": ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Please enter a number from 1 to 3")
        else:
            print("Please enter a number from 1 to 3")
    
    return lines

def get_bet():
    while True:
        bet = input("How much money do you want to bet? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a bet number from {MIN_BET} to {MAX_BET}")
        else:
            print("Please enter a number to bet")
    
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet >= balance:
            print(f"My friend, you don't have enough money for that bet. Your current deposit is ${balance}.")
        else:
            break
    print(f"Your balance is ${balance} and your total bet is ${total_bet}")

main()