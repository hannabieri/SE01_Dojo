def display_board(board):
    print("\n|1|2|3|4|5|6|7|")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|" + board[10] + "|" + board[11] + "|" + board[12] + "|" + board[13] + "|")
    print("|" + board[14] + "|" + board[15] + "|" + board[16] + "|" + board[17] + "|" + board[18] + "|" + board[19] + "|" + board[20] + "|")
    print("|" + board[21] + "|" + board[22] + "|" + board[23] + "|" + board[24] + "|" + board[25] + "|" + board[26] + "|" + board[27] + "|")
    print("|" + board[28] + "|" + board[29] + "|" + board[30] + "|" + board[31] + "|" + board[32] + "|" + board[33] + "|" + board[34] + "|")
    print("|" + board[35] + "|" + board[36] + "|" + board[37] + "|" + board[38] + "|" + board[39] + "|" + board[40] + "|" + board[41] + "|")


def check_input(user_input):
    if 1 <= user_input <= 7:
        return True
    else:
        print("\nUh-ohh. Enter a number between 1 and 9.")


def get_next_player(player_active):
    if player_active == "O":
        return "X"
    else:
        return "O"


def check_winner(new_board):
    x_wins = "\n\n---- !!!! X wins !!!! ----"
    o_wins = "\n\n---- !!!! O wins !!!! ----"

    for n in range(0,41):
        if n % 7 in [0,1,2,3]:
            if all(new_board[n + i] == "X" for i in [0,1,2,3]):
                print(x_wins)
                game_active = False
            if all(new_board[n + i] == "O" for i in [0,1,2,3]):
                print(o_wins)
                game_active = False

            #for the diagonale to the right
            if n <= 20:
                if all(board[n + i] == "X" for i in [0,8,16,24]):
                    print(x_wins)
                    game_active = False
                if all(board[n + i] == "O" for i in [0,8,16,24]):
                    print(o_wins)
                    game_active = False

        #for the column
        if n <= 20:
            if all(board[n + i] == "X" for i in [0,7,14,21]):
                print(x_wins)
                game_active = False
            if all(board[n + i] == "O" for i in [0,7,14,21]):
                print(o_wins)
                game_active = False

        #for the diagonale to the left
        if n % 7 in [3,4,5,6] and n <= 20:
            if all(board[n + i] == "X" for i in [0,6,12,18]):
                print(x_wins)
                game_active = False
            if all(board[n + i] == "O" for i in [0,6,12,18]):
                print(o_wins)
                game_active = False



def play_game(game_active, board, player_active):
    new_board = board.copy()
    while game_active:
        user_input = input(f"\nYour move, player {player_active}. Enter the column you want to drop your piece: ")
        user_input = int(user_input)
        #user_input = 1

        if check_input(user_input):
            for n in range(5, -1, -1):
                
                if new_board[(user_input-1)+(7*n)] == " ":
                    new_board[(user_input-1)+(7*n)] = player_active
                    check_winner(new_board)
                    player_active = get_next_player(player_active)
                    break

                #elif new_board[(user_input-1) == "X" or new_board[(user_input-1) == "O":
                
            else:
                print("\n\n---- !!!! That row was already full! Try another one. !!!! ----")
  
        display_board(new_board)
        



'''
------------------------------------------------------------------------

HERE COMES THE GAME 

------------------------------------------------------------------------
'''



game_active = True
player_active = "O"

#Create board 7x6
board = [" ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " "]

print("Hello and welcome to the game! Enter the number of the row you want to drop your stone.\n")
display_board(board)
play_game(game_active, board, player_active)




