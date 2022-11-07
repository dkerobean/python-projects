import random

#Defining constant variables
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3
#number of symbols to choose from
symbols = {
    "A": 2,
    "B": 5,
    "C": 4,
    "D": 6
}

symbol_value = {
    "A": 23,
    "B": 150,
    "C": 90,
    "D": 15
}


#check if the user has won and determine amount won
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        #checking throgh all the columns to see if they are the same
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                #check winning lines
                winning_lines.append(line + 1)
        return winnings, winning_lines


#function to generate outcome of the slot machine using the symbols
def get_spin(cols,rows,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

#selecting what values to go into every single column
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


#print results of slot machine unto screen
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            #print "|" inbetween and empty space at the end
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row],end=" ")

        print()


#function to take deposit from user
def take_deposit():
    while True:
        amount = input("Please enter the amount you want to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than 0")

        else:
            print("Please Enter A Number")
    return amount

#get number of lines user bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1 - {MAX_LINES})")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid number of lines")

        else:
            print("please enter a number")
    return lines

#get user bet and check if it its a valid bet (min & max bet)
def get_user_bet():
    while True:
        user_bet = input("How much would you like to bet on each line? $")
        if user_bet.isdigit():
            user_bet = int(user_bet)
            if MIN_BET <= user_bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a valid amount")

    return user_bet

#running multiple times and reducing user balance
def spin(balance):
    lines = get_number_of_lines()
    while True:
        user_bet = get_user_bet()
        total_bet = user_bet * lines
        if total_bet > balance:
            print(f"You do not have enough money to place this bet. Your balance is {balance}")
        else:
            break

    print(f"You are betting ${user_bet} on {lines} lines. Your total bet is {total_bet}")

    slots = get_spin(ROWS, COLS, symbols)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, user_bet, lines, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:  {winning_lines}")

    return winnings - total_bet


#main function to call the program again whenever we need it
def main():
    balance = take_deposit()
#check if bet is within users balance
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press any key to continue (q to quit)")
        if answer.lower() == "q":
            break
        else:
            balance += spin(balance)
main()

