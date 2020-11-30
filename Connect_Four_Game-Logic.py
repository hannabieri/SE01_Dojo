def play_game(game_active, board, player_active):
    new_board = board.copy()
    if game_active:
        #user_input = input(f"\nYour move, player {player_active}. Enter the column you want to drop your piece: ")
        #user_input = int(user_input)
        user_input = 1
        #print(list(reversed(range(6))))
        for n in range(5, -1, -1):
            print(n)
            if new_board[(user_input-1)+(7*n)] == " ":
                new_board[(user_input-1)+(7*n)] = player_active

            else:
                print("\n\n---- !!!! That row was already full! Try another one. !!!! ----")





game_active = True
player_active = "O"
#Create board 7x6
board = [" ", " ", " ", " ", " ", " ", " ",
        " ", " ", "O", " ", " ", " ", " ",
        " ", " ", "O", " ", " ", " ", " ",
        " ", " ", "X", " ", " ", " ", " ",
        " ", " ", "O", " ", " ", " ", " ",
        " ", "X", "X", "X", " ", " ", " "]

play_game(game_active, board, player_active)


'''
def play_game(game_active, board, player_active):
    new_board = board.copy()
    while game_active:
        user_input = input(f"\nYour move, player {player_active}. Enter the column you want to drop your piece: ")
        user_input = int(user_input)
        #user_input = 3
        if check_input(user_input):

            if new_board[(user_input-1)+(7*5)] == " ":
                new_board[(user_input-1)+(7*5)] = player_active
                check_winner(new_board)
                player_active = get_next_player(player_active)

            elif new_board[(user_input-1)+(7*4)] == " ":
                new_board[(user_input-1)+(7*4)] = player_active
                check_winner(new_board)
                player_active = get_next_player(player_active)

            elif new_board[(user_input-1)+(7*3)] == " ":
                new_board[(user_input-1)+(7*3)] = player_active
                check_winner(new_board)
                player_active = get_next_player(player_active)

            elif new_board[(user_input-1)+(7*2)] == " ":
                new_board[(user_input-1)+(7*2)] = player_active
                check_winner(new_board)
                player_active = get_next_player(player_active)

            elif new_board[(user_input-1)+(7*1)] == " ":
                new_board[(user_input-1)+(7*1)] = player_active
                check_winner(new_board)
                player_active = get_next_player(player_active)

            elif new_board[(user_input-1)+(7*0)] == " ":
                new_board[(user_input-1)+(7*0)] = player_active
                check_winner(new_board)
                player_active = get_next_player(player_active)

            else:
                print("\n\n---- !!!! That row was already full! Try another one. !!!! ----")

        
        
        display_board(new_board)
    '''