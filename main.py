"""
This is the simple battle ship game:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
this is the board. You will have 4 hints to win. Guess where the battle ship is and
sunk it!
My ship will deal damage to you. So, look out!

Good luck!

"""

from random import randint

board = []
health = 100
hint = 4

for x in range(0, 7):
    board.append(["O"] * 7)


def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def print_board(board):
    for row in board:
        for col in row:
            if col == 'X':
                print('\x1b[6;30;42m' + col + '\x1b[0m', end='')
                print('\x1b[4;30;47m' + ' ' + '\x1b[0m', end='')
            elif col == 'B':
                print('\x1b[0;33;41m' + col + '\x1b[0m', end='')
                print('\x1b[4;30;47m' + ' ' + '\x1b[0m', end='')
            else:
                print('\x1b[4;30;47m' + col + '\x1b[0m', end='')
                print('\x1b[4;30;47m' + ' ' + '\x1b[0m', end='')

        print()


print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


def dir_atk(guess_row, guess_col):
    if guess_row < ship_row:
        if guess_col < ship_col:
            return "Atk from bottom!" + " and from right"
        elif guess_col > ship_col:
            return "Atk from bottom!" + " and from left"
        elif guess_col == ship_col:
            return "Atk from bottom!"
    elif guess_row > ship_row:
        if guess_col < ship_col:
            return "Atk from top!" + " and from right"
        elif guess_col > ship_col:
            return "Atk from top!" + " and from left"
        elif guess_col == ship_col:
            return "Atk from top!"
    else:
        if guess_col < ship_col:
            return "Atk from right"
        elif guess_col > ship_col:
            return "Atk from left"


def hint_give(guess_row, guess_col, hint=hint):
    print_board(board)
    while 1:
        hint_need = input("Do you want a hint? Enter 'Y' or 'N' ").upper()
        if hint_need == 'Y':
            if hint >= 1:
                print(dir_atk(guess_row, guess_col))
                hint -= 1
            else:
                print("You don't have any hint left!")
            break
        elif hint_need == 'N':
            print("Brave soldier! Keep going!")
            break
        elif hint_need == '19980815':
            print("Cheat mode enabled! Unlimited hint! Unlimited Health!")
            health = 1000000
            hint = 100000
            break
        else:
            print("Please, Please, enter 'y' or 'n'")
            continue


while 1:
    while 1:
        guess_row = input("Guess Row: ")
        if is_num(guess_row):
            guess_row = int(guess_row)
            break
        else:
            print("Please enter a number!")
            continue
    while 1:
        guess_col = input("Guess Col: ")
        if is_num(guess_col):
            guess_col = int(guess_col)
            break
        else:
            print("Please enter a number!")
            continue
    print('\x1b[5;30;42m' + "Health remaining: " + '\x1b[0m', end='')
    print('\x1b[6;30;45m' + str(health) + '\x1b[0m')
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        board[ship_row][ship_col] = 'B'
        print_board(board)
        break
    else:
        if guess_row not in range(7) or \
                        guess_col not in range(7):
            print("Oops, that's not even in the ocean.")
            print("My battle ship shoots you!!")
            health -= 10
            if health <= 0:
                print("you died!")
                break

            hint_give(guess_row, guess_col)



        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
            print("My battle ship shoots you!!")
            health -= 10
            if health <= 0:
                print("you died!")
                break
            hint_give(guess_row, guess_col)
        else:
            print("You missed my battleship!")
            print("My battle ship shoots you!!")
            board[guess_row][guess_col] = "X"
            health -= 10
            if health <= 0:
                print("you died!")
                break
            hint_give(guess_row, guess_col)
