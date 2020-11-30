board = [" ", " ", " ", " ", " ", " ", " ",
        " ", " ", "", " ", " ", " ", " ",
        " ", " ", "O", " ", " ", "X", " ",
        " ", " ", "O", " ", "X", " ", " ",
        " ", " ", "O", "X", " ", " ", " ",
        " ", "X", "X", " ", "X", " ", " "]


def check_winner(board):
    for n in range(0,41):
        #for the row
        if n % 7 in [0,1,2,3]:
            if all(board[n + i] == "X" for i in [0,1,2,3]):
                print("X wins")
            if all(board[n + i] == "O" for i in [0,1,2,3]):
                print("O wins")

            #for the diagonale to the right
            if n <= 20:
                if all(board[n + i] == "X" for i in [0,8,16,24]):
                    print("X wins")
                if all(board[n + i] == "O" for i in [0,8,16,24]):
                    print("O wins")

        #for the column
        if n <= 20:
            if all(board[n + i] == "X" for i in [0,7,14,21]):
                print("X wins")
            if all(board[n + i] == "O" for i in [0,7,14,21]):
                print("O wins")

        #for the diagonale to the left
        if n % 7 in [3,4,5,6] and n <= 20:
            if all(board[n + i] == "X" for i in [0,6,12,18]):
                print("X wins")
            if all(board[n + i] == "O" for i in [0,6,12,18]):
                print("O wins")

check_winner(board)
