board = ["A", "B", "C",
		"D", "E", "F",
		"G", "~", "H"]

user_index = 4

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
	print(logic.get(user_index))
	print(board.index("~"))
	if board.index("~") in logic.get(user_index):
		return True

print(check_input(user_index))


board = ["A", "B", "C", "D", 
		"E", "F", "G", "~", 
		"H", "I", "J", "K",
		"L", "M", "N", "O"]

user_index = 4

def check_input_16(user_index):
	logic = {
		0: [1, 4],
		1: [0, 2, 5],
		2: [1, 3, 6],
		3: [2, 7],
		4: [0, 5, 8],
		5: [1, 4, 6, 9],
		6: [2, 5, 7, 10],
		7: [3, 6, 11],
		8: [4, 9, 12],
		9: [5, 8, 10, 13],
		10: [6, 9, 11, 14],
		11: [7, 10, 15],
		12: [8, 13],
		13: [9, 12, 14],
		14: [10, 13, 15],
		15: [11, 14],
	}
	print(logic.get(user_index))
	print(board.index("~"))
	if board.index("~") in logic.get(user_index):
		return True
	else: 
		return "Can't be moved"
		
print(check_input_16(user_index))
