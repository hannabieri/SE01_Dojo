game_active = True

board = ["~", "B", "C",
		"D", "E", "F",
		"G", "A", "H"]



def display_board(board):
	print(board[0] + "|" + board[1] + "|" + board[2])
	print(board[3] + "|" + board[4] + "|" + board[5])
	print(board[6] + "|" + board[7] + "|" + board[8])
	return

# Main game logic
def play_game(game_active, board):
	while game_active:
		user_input = input("\n. . .\n\nWhich letter do you want to move? Enter here: ")

		if user_input == "q":
			print("Oki, goodbye!")
			game_active = False

		else:
			user_index = indexing_input(user_input)

			if check_input(user_index):
				empty_field = board.index("~")
				board = swap_positions(board, user_index, empty_field)
				display_board(board)

				if check_result(board):
					print("\n-------------------\n!! You are a born winner! Congrats !!\n-------------------\n")
					play_again = input("Want to play again? Enter y / n. ")
					if play_again.lower() == "n":
						print("Oki, goodbye!")
						game_active = False
					else: 
						board = ["H", "~", "C", "F", "E", "D", "A", "B", "G"]
			else:
				print("Upsi, that letter can't move. Try another one!")


# Mapping user's input (letter, string) to board index (number, int)
def indexing_input(user_input):
	user_input = user_input.upper()
	try:
		return board.index(user_input)
	except ValueError:
		print("That character does not seem to exist on the board.")


# Check if move is possible by taking entered field and checking if empty is next to it
def check_input(user_index):
	logic = {
		0: [1, 3],
		1: [0, 2, 4],
		2: [1, 5],
		3: [0, 4, 6],
		4: [1, 3, 5, 7],
		5: [2, 4, 8],
		6: [3, 7],
		7: [4, 6, 8],
		8: [5, 7],
	}
	if board.index("~") in logic.get(user_index):
		return True

# Swaps the user_index and the empty_field (by number)
def swap_positions(board, pos1, pos2):
	board[pos1], board[pos2] = board[pos2], board[pos1] 
	return board

# Checks if current state of board is end solution
def check_result(board):
	board_result = ["A", "B", "C", "D", "E", "F", "G", "H", "~"]
	if board == board_result:
		return True



'''
------------------------------------------------------------------------------------
!!! HERE STARTS THE GAME !!!
------------------------------------------------------------------------------------
'''


print("\n-------------------\nHello and welcome! \nYou can move the letters next to the free square (). \nThe goal is to have all letter is alphabetical order, the empty field at the end. \nYou can exit the game by entering q.\n\tGood luck!\n-------------------") 
display_board(board)


play_game(game_active, board)















