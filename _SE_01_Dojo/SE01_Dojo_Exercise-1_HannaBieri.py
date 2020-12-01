# Beaker starting state, nested list
beaker = [[], [1, 0, 0], [2, 1, 2], [2, 1, 0]]

# Function to display beaker to user
def create_beaker(beaker):
	print("Beaker 1:", beaker[1][0], "|", beaker[1][1], "|", beaker[1][2])
	print("Beaker 2:", beaker[2][0], "|", beaker[2][1], "|", beaker[2][2])
	print("Beaker 3:", beaker[3][0], "|", beaker[3][1], "|", beaker[3][2])


# Creating function to convert input (sting) into integer
def parse_input(user_input):
    return int(user_input)


def check_if_legal(move_from, move_into):
		# Figure out how many units are free in the beaker to move into 
		count_empty_units = beaker[move_into].count(0)
		print(f"This many units are free: {count_empty_units}")
		
		# Figure out how many units are occupied in the beaker to move from 
		count_full_units = beaker[move_from].count(1) + beaker[move_from].count(2)
		print(f"This many units are occupied: {count_full_units}")

		# If there is more space than has to be moved: True
		if count_empty_units >= count_full_units:
			
			#Figure out if colors (numbers) match by getting index of item on top
			if beaker[move_into][2-count_empty_units] == beaker[move_from][count_full_units-1]:
				print(beaker[move_into][2-count_empty_units])
				print(beaker[move_from][count_full_units-1])
				# Both checks passed, space and color fit!
				return True



def play_game(beaker):
		create_beaker(beaker)
		
		#user_input_1 = input("\nEnter the beaker to move liquid from: ")
		user_input_1 = "1"
		#user_input_2 = input("Enter the beaker to move liquid into: ")
		user_input_2 = "3"

		# Calling function for input (sting) into int
		move_from = parse_input(user_input_1)
		move_into = parse_input(user_input_2)

		if check_if_legal(move_from, move_into):
			print("Hooray, legal move!")
			
		else:
			print("\nAi, ai... Unfortunately, that move is not possible! :( \n")


print("\n\nWelcome to the Watersort game!\n")
play_game(beaker)




