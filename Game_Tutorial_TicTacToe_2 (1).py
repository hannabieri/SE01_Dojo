game_active = True
player_active = "X"

board = ["",
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]


print("\n---------------\n\nWelcome to a fabulous game of Tic Tac Toe! \
    \nYou can stop the game by entering q. \n\t\t\tHave fun!")


def display_board():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

print(display_board())

def parse_input(user_input):
    return int(user_input)

def check_input(user_input):    
    if 1 <= user_input <= 9:
        try: 
            pass
        except ValueError:
            print("ValueError – Enter a number between 1 and 9.")
        else: 
            if board[user_input] == "X" or board[user_input] == "O":
                print("\tThat square is already taken. Try another one.")
            else: 
                return True
    else:
        print("\tUh-ohh. Enter a number between 1 and 9.")


def get_next_player(player_active):
    if player_active == "X":
        return "O"
    else:
        return "X"



def check_winner():
    return board[1] == board[2] == board[3] or\
    board[4] == board[5] == board[6] or\
    board[7] == board[8] == board[9] or\
    board[1] == board[4] == board[7] or\
    board[2] == board[5] == board[8] or\
    board[3] == board[6] == board[9] or\
    board[1] == board[5] == board[9] or\
    board[7] == board[5] == board[3]



while game_active:
    user_input = input(f"\nPlayer {player_active}! \n---------------\nWhat's your move? Enter number here: ")
    if user_input == 'q':
        game_active = False
        print("Awwww.. See you again!")
        break
    user_input = parse_input(user_input)
        # Checks everythin in check_input function, and returns true if it is true
    if check_input(user_input):
        #exchange value on board with player
        board[user_input] = player_active
        display_board()

        if check_winner():
            print(f"\n-o-o-o-o-o-o-o-\nPlayer {player_active} has won!! Congrats!\n-o-o-o-o-o-o-o-")
            play_again = input("Want to play again? Answer y / n: ")
            if play_again.lower() == "y":
                print("\n---------------\nOkay, let's restart the game!")
                board = ["",
                        "1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9"]
            else:
                print("Okidoki, byeeee.")
                game_active = False
        
        player_active = get_next_player(player_active)


        








