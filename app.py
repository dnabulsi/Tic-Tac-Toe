from os import system

rows = {'top':['1', ' | ', '2', ' | ', '3'], 'dashes1':['- + - + -'], 'middle':['4', ' | ', '5', ' | ', '6'], 'dashes2':['- + - + -'], 'bottom':['7', ' | ', '8', ' | ', '9']}
row_names = ['top','middle','bottom']
numbers = ['1','2','3','4','5','6','7','8','9']

def printer():
    print(end='\n')
    for row in rows:
        for element in rows[row]:
            print(element,end='')
        print(end='\n')
    print(end='\n')

def user_choice(XorO):
    while True:
        pos = input(f"PLAYER {XorO}'S TURN: Select a position (1 - 9 if available on board): ")
        if pos.isdigit() == True:
            if int(pos) in range(1,10) and str(pos) in numbers:
                return str(pos)
        print("That is not available! Try again.")

def starting_player():
    while True:
        letter = input("\nSelect the starting player, X or O: ").upper()
        if letter == 'X' or letter == 'O':
            return letter
        print("Invalid input! Try again.")
    
def replace_number(letter, pos):
    for element in rows:
        for x in range(len(rows[element])):
            if rows[element][x] == pos:
                if letter == 'X':
                    rows[element][x] = 'X'
                    return 'O'
                else:
                    rows[element][x] = 'O'
                    return 'X'
            continue

def pattern_checker():
    return numbers[0] == numbers[1] == numbers[2] or numbers[3] == numbers[4] == numbers[5] or numbers[6] == numbers[7] == numbers[8] or numbers[0] == numbers[3] == numbers[6] or numbers[1] == numbers[4] == numbers[7] or numbers[2] == numbers[5] == numbers[8] or numbers[0] == numbers[4] == numbers[8] or numbers[2] == numbers[4] == numbers[6]

def game():

    print("Welcome to Tic Tac Toe! Let's begin...\n")

    # Initialize starting letter
    XorO = starting_player()

    for x in range(9):   
        
        system('cls||clear')
        
        # Print tic tac toe table
        printer()

        # Initialize user choice from position from table, number as string data type
        pos = user_choice(XorO)

        # Remove number from numbers list for positions
        numbers[int(pos) - 1] = XorO

        # Replace number on table with player's letter, return new letter
        XorO= replace_number(XorO, pos)

        if pattern_checker():
            system('cls||clear')
            printer()
            if XorO == 'X':
                print("\nTHE WINNER IS O!\n")
                quit()
            else:
                print("\nTHE WINNER IS X!\n")
                quit()

    print("\nIT'S A TIE!\n")

game()