squares = {
	1: "C",
	2: "B",
	3: "A",
	4: "C",
	5: "A",
	6: "B"
}

for key in squares.keys():
	print(key)

print(squares[1] + " | " + squares[2] + " | " + squares[3]) 
print(squares[4] + " | " + squares[5] + " | " + squares[6]) 

def display_board():
	print("1" + " | " + "2" + " | " + "3") 
	print("4" + " | " + "5" + " | " + "6") 


user_input_1 = "1"
user_input_2 = "4"

user_input_1 = int(user_input_1)
user_input_2 = int(user_input_2)

if squares[user_input_1] == squares[user_input_2]:
	print("hooray! + remove")
	#replace number with squares[1] squares[4]

else: 
	print("turn back around")
print({squares[user_input_1]}, {squares[user_input_2]})


display_board()



