'''def dirReduc(a):
	directions_given = a.copy()
	reducable_directions = [["NORTH", "SOUTH"],["SOUTH", "NORTH"],["EAST", "WEST"],["WEST", "EAST"]]
	print(check_subset(directions_given,reducable_directions))
	# while check_reducable(directions_given):
	# 	print("hooray")

def check_subset(directions_given, reducable_directions):
	return all(map(directions_given.__contains__, reducable_directions)) 

	# reduce_directions = {
	#     "L1": ["NORTH", "SOUTH"],
	#     "L2": ["SOUTH", "NORTH"],
	#     "L3": ["EAST", "WEST"],
	#     "L4": ["WEST", "EAST"],
	#     }
	
	

# def reduce():
# 	reducable_directions = [["NORTH", "SOUTH"],["SOUTH", "NORTH"],["EAST", "WEST"],["WEST", "EAST"]]
# 	while reducable_directions in directions_given:



	    
print(dirReduc(a))
'''


# def check_subset(dogs, dogs_subset):
# 	return all(x in dogs for x in dogs_subset)
#  	# return any(
#   #       dogs[i:i+len(dogs_subset)] == dogs_subset
#   #       for i in range(len(dogs) - len(dogs_subset) + 1))

# dogs = ["wuffi", "bello", "schnuffi", "bello"]
# dogs_subset = ["wuffi", "bello"]
# print(check_subset(dogs, dogs_subset))



def check_subset(directions_given):
	L1 = ["NORTH", "SOUTH"]
	L2 = ["SOUTH", "NORTH"]
	L3 = ["EAST", "WEST"]
	L4 = ["WEST", "EAST"]
	
	if all(x in directions_given for x in L1):
		return L1
	if all(x in directions_given for x in L2):
		return L2
	if all(x in directions_given for x in L3):
		return L3
	if all(x in directions_given for x in L4):
		return L4

directions_given = ["SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(check_subset(directions_given))



