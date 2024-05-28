import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count = {
    "🦀": 2,
    "🥕": 4, 
    "🌻": 6,
    "💧": 8
}

symbol_values = {
    "🦀": 5,
    "🥕": 4, 
    "🌻": 3,
    "💧": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    #check the winning lines so we can print those at the end of the game
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) #+1 bc its an index and we want to show the real number
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    #Create a list with all the symbols and the times they can appear, we will randomly pick from those
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items() displays both the key (symbol) and value(symbol_count)
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #Create columns of symbols, use a copy so we make sure the respect the number of symbols and dont use more than exist
    columns = []
    for _ in range(cols):
        column = []
        #COPY OF ALL_SYMBOLS, then remove the chosen symbol from the list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            #Add chosen value to the col that will be displayed
            column.append(value)
        #When the col is done, append it to the 3 cols that will be displayed
        columns.append(column)
    return  columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        #We want to print the symbol with a slash for separation, but not in the third symbol. This is where .enumarate() comes in handy, because it provides an index(i)
        for i, column in enumerate(columns):
            if i != len(columns):
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

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

def spin(balance):
    lines = get_number_of_lines()
    while True:
            bet = get_bet()
            total_bet = bet * lines
            if total_bet >= balance:
                print(f"My friend, you don't have enough money for that bet. Your current deposit is ${balance}.")
            else:
                break
    print(f"Your balance is ${balance} and your total bet is ${total_bet}")

    #TIME TO GENERATE THE SLOTS!! (slots = cols)
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    #GET WINNINGS AND PRINT THEM
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    winning_lines_str = ', '.join(map(str, winning_lines))

    print(f"Yayyy you won ${winnings} in the following lines: {winning_lines_str}🥳")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    

main()