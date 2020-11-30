game_active = True
# board = [
# 	  [{"letter": "C", "hidden": True}, {"letter": "B", "hidden": True}, {"letter": "C", "hidden": True}],
# 	  [{"letter": "A", "hidden": True}, 	{"letter": "A", "hidden": True}, 	{"letter": "B", "hidden": True}]
# 	  ]

board = [[""], ["C", 1], ["B", 2], ["C", 3], ["A", 4], ["A", 5], ["B", 6]]


def parse_input(user_input):
    return int(user_input)

def display_board(board):
	print(board[1][1], " | ",  board[2][1],  " | ",  board[3][1]) 
	print(board[4][1],  " | ",  board[5][1],  " | ",  board[6][1]) 


while game_active:
	display_board(board)

	user_input_1 = input("Enter the first card to turn: ")#"4"
	user_input_2 = input("Enter the second card to turn: ")#"5"
	parsed_1 = parse_input(user_input_1)
	parsed_2 = parse_input(user_input_2)
	print(parsed_1, parsed_2)

	

	if board[parsed_1][0] == board[parsed_2][0]:
		print("\n---------------------\nIt's a match!!")
		board[parsed_1][1] = board[parsed_1][0]
		board[parsed_2][1] = board[parsed_2][0]
		#display_board(board)


	# for row in board:
	# 	for column in row:
	# 		print(column)

			
	
		#print(i)
		#board['hidden'] = False


	




# if user_input_1 == user_input_2:
# 	print("hooray! + remove")
# 	#replace number with squares[1] squares[4]

# else: 
# 	print("turn cards back around")


# display_board()




'''
game_active = True
board = [
	  [{"letter": "D", "hidden": True}, {"letter": "B", "hidden": False}, {"letter": "E", "hidden": True}, {"letter": "F", "hidden": True}],
	  [{"letter": "A", "hidden": True}, 	{"letter": "A", "hidden": True}, 	{"letter": "F", "hidden": False}, 	{"letter": "D", "hidden": True}],
	  [{"letter": "C", "hidden": True}, {"letter": "C", "hidden": False}, {"letter": "B", "hidden": False}, {"letter": "E", "hidden": True}]
	]
'''
