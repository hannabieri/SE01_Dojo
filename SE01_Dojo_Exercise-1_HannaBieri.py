# Beaker starting state, nested list
beaker = [[], [2, 0, 0], [1, 2, 2], [2, 1, 0]]

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
	
	# Figure out how many units are occupied in the beaker to move from 
	count_full_units = beaker[move_from].count(1) + beaker[move_from].count(2)

	#Figure out if colors (numbers) match of both beakers by getting index of item on top
	if beaker[move_into][2-count_empty_units] == beaker[move_from][count_full_units-1]:

		# Check if there index next to it is the same value (move two units together)
		if beaker[move_from][count_full_units-1] == beaker[move_from][count_full_units-2]:
			# Check if there is more space than has to be moved
			if count_empty_units >= 2:
				return True

		# Check if there index next to it is the same value (move two three together)
		elif beaker[move_from][count_full_units-1] == beaker[move_from][count_full_units-2] == beaker[move_from][count_full_units-3]:
			# Check if there is more space than has to be moved
			if count_empty_units >= 3:
				return True

		# Move one unit
		else:
			# Check if there is more space than has to be moved
			if count_empty_units >= 1:
				return True			



def play_game(beaker):
	create_beaker(beaker)
	
	user_input_1 = input("\nEnter the beaker to move liquid from: ")
	#user_input_1 = "1"
	user_input_2 = input("Enter the beaker to move liquid into: ")
	#user_input_2 = "2"

	# Calling function for input (sting) into int
	move_from = parse_input(user_input_1)
	move_into = parse_input(user_input_2)

	if check_if_legal(move_from, move_into):
		print("Hooray, legal move!")
		
	else:
		print("\nAi, ai... Unfortunately, that move is not possible! :( \n")


print("\n\nWelcome to the Watersort game!\n")
play_game(beaker)




