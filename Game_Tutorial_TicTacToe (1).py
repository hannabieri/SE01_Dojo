'''
Learnings from this tutorial:

to execute/link to a function in a while loop:
«move = user_input()
    if move:»

and learning: this just checks is winning is TRUE and executes if it is
    «if winning: »


global:
    accesses variable from everywhere, so also outside of function!



'''


# Trick to not have index 0 but 1 matching 1
game_active = True
current_player = 'X'

board = ["",
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]


def display_board():
    print (board[1] + "|" + board[2] + "|" + board[3] + "|")
    print (board[4] + "|" + board[5] + "|" + board[6] + "|")
    print (board[7] + "|" + board[8] + "|" + board[9] + "|")


def changing_players():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def user_input():
    # global keyword allows modifying the variable outside of the current scope !!
    global game_active
    while True:
        move = input("Please enter your move here: ")
        if move.lower() == 'q':
            game_active = False
            return
        #checks first if it is a numerical value
        try:
            move = int(move)
        except ValueError:
            print("No, no... Please enter number between 1 to 9.")
        else: 
            if move >= 1 and move <= 9:
                if board[move] == 'X' or board[move] == 'O':
                    print("This is already taken, my friend. Try another!")
                else:
                    return move
            else: 
                print("Number needs to be between 1 and 9.")


def check_for_winner():
    # Rows
    if board[1] == board[2] == board[3]:
        return board[1]
    if board[4] == board[5] == board[6]:
        return board[4]
    if board[7] == board[8] == board[9]:
        return board[7]
    # Columns
    if board[1] == board[4] == board[7]:
        return board[1]
    if board[2] == board[5] == board[8]:
        return board[2]
    if board[3] == board[6] == board[9]:
        return board[3]
    # Diagonale
    if board[1] == board[5] == board[9]:
        return board[5]
    if board[7] == board[5] == board[3]:
        return board[5]


# Game will run as long as this is 'True'
while game_active:
    print(f"\n\n----------------------------\nPlayer {current_player}'s move")
    # Entry of active player
    move = user_input()
    if move:
        # Accesses according index on board (by using move, e.g. 2) 
        # and replaces it with X or O !
        board[move] = current_player
        # Display current board
        display_board()
        # Check for winner
        winning = check_for_winner()
        if winning:
            print(f"Player {winning} has won!")
            another_one = input("Wanna go again? Enter y / n: ")
            if another_one.lower() == 'y':
                game_active = True        
                # THIS DOES NOT REALLY WORK !!!!        
            else:
                print("Byeeeeeee!")
                game_active = False
        # Change player
        changing_players()





