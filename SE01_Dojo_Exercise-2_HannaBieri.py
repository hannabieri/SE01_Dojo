# Function to display beaker to user
def display_beaker(beaker):
	print("Beaker 1:", beaker[1][0], "|", beaker[1][1], "|", beaker[1][2])
	print("Beaker 2:", beaker[2][0], "|", beaker[2][1], "|", beaker[2][2])
	print("Beaker 3:", beaker[3][0], "|", beaker[3][1], "|", beaker[3][2])


# Creating function to convert input (sting) into integer
def parse_input(user_input):
    return int(user_input)


# RETURNS the TOP color (eg. 1 or "1") move_from
def get_top_color(beaker, move_orig):
	if beaker[move_orig][2] == 2:
		return 2
	elif beaker[move_orig][2] == 1:
		return 1
	#move to middle one if top one empty
	elif beaker[move_orig][2] == 0:

		if beaker[move_orig][1] == 2:
			return 2
		elif beaker[move_orig][1] == 1:
			return 1
		#move to bottom one if middle and top are empty
		elif beaker[move_orig][1] == 0:

			if beaker[move_orig][0] == 2:
				return 2
			elif beaker[move_orig][0] == 1:
				return 1
			# all empty
			elif beaker[move_orig][0] == 0:
				return 0


# RETURNS the number of TOP color
def get_top_color_quantity(beaker, move_from, colour_to_move):
  	
  	# Check if there index next to it is the same value (move two units together)
	if ((beaker[move_from][2] and beaker[move_from][1]) == colour_to_move) or ((beaker[move_from][2] == 0) and \
		(beaker[move_from][1] and beaker[move_from][0]) == colour_to_move):
		return 2

	# Check if there index next to it is the same value (move two three together)
	elif (beaker[move_from][2] and beaker[move_from][1] and beaker[move_from][0]) == colour_to_move:
		return 3

	# Move one unit
	else:
		return 1			



# RETURNS the number of available spaces move_into
def get_available_space(beaker, move_into):  
	count_empty_units = beaker[move_into].count(0)
	return count_empty_units






def play_game(beaker):
	display_beaker(beaker)
	
	if game_active:
		#user_input_1 = input("\nEnter the beaker to move liquid from: ")
		user_input_1 = "3"
		#user_input_2 = input("Enter the beaker to move liquid into: ")
		user_input_2 = "1"

		# Calling function for input (sting) into int
		move_from = parse_input(user_input_1)
		move_into = parse_input(user_input_2)

		colour_to_move = get_top_color(beaker, move_from)
		units_to_move = get_top_color_quantity(beaker, move_from, colour_to_move)
		units_available = get_available_space(beaker, move_into)

		# Check if the colours match
		if get_top_color(beaker, move_from) == get_top_color(beaker, move_into):
			print("Hooray, legal move!")
			# Check if space available
			if get_top_color_quantity(beaker, move_from, colour_to_move) <= get_available_space(beaker, move_into):
			 	print("Space matches!")
			 	print(units_to_move)
			 	if (beaker[move_from][2] != 0) and (units_to_move == 1) and (beaker[move_into][1] != 0):
			 		beaker[move_into][2] = beaker[move_from][2]
			 		beaker[move_from][2] = 0
			 	elif (beaker[move_from][1] != 0) and (units_to_move == 1) and (beaker[move_into][1] != 0):
			 		beaker[move_into][2] = beaker[move_from][2]
			 		beaker[move_from][2] = 0

			display_beaker(beaker)

		# this means beaker is empy
		elif units_available == 3:
			pass
			

		else:
			print("\nAi, ai... Unfortunately, that move is not possible! :( \n")



# Beaker starting state, nested list
game_active = True
beaker = [[], [1, 0, 0], [2, 1, 2], [2, 1, 0]]

# Welcome and initialize game
print("\n\nWelcome to the Watersort game!\n")
play_game(beaker)











		# colour_to_move = get_top_color(beaker, move_from)
		# # print(f"Colour to move: {colour_to_move}")
		# # units_to_move = get_top_color_quantity(beaker, move_from, colour_to_move)
		# # print(f"Units to move: {units_to_move}")
		# units_available = get_available_space(beaker, move_into)
		# # print(f"Units available: {units_available}")





# def check_if_legal(beaker, move_from, move_into, colour_to_move, units_to_move, units_available):
# 	# Check from_beaker is not empty
# 	print(colour_to_move)
# 	if colour_to_move != 0:
# 		#Figure out if colors (numbers) match of both beakers by getting the item on top
# 		pass

# 	# else it is empty, so anything can go in
# 	else:
# 		print("Empty one!")
# 		pass

# # 	# Figure out how many units are occupied in the beaker to move from 
# # 	count_full_units = beaker[move_from].count(1) + beaker[move_from].count(2)

# # 	#Figure out if colors (numbers) match of both beakers by getting index of item on top
# # 	if beaker[move_into][2-count_empty_units] == beaker[move_from][count_full_units-1]:
# # 		pass


