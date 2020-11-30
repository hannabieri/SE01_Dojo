game_active = True
word = [["B", "-"], ["A", "-"], ["N", "-"], ["A", "-"], ["N", "-"], ["A", "-"]]

def parse_input(user_input):
    return int(user_input)

def display_word(word):
	print("This is the word to guess: ")
	print(word[0][1], word[1][1], word[2][1], word[3][1], word[4][1], word[5][1]) 


if game_active:
	display_word(word)
	#input_letter = input("\nWhich letter do you guess? Answer here: ")
	input_letter = "a"

	if len(input_letter) == 1:
		input_letter = input_letter.upper()

		for nested_element in word:
			print(nested_element)
			print(word.index(nested_element))
			if input_letter in nested_element:
				# Counting appearances of input in string
				# count = nested_element.count(input_letter)
				# print(f"\nIt's a match! Your letter {input_letter} appears {count} times.\n")

				#print(word.index(nested_element))
				#print(nested_element[0])
        	#    return word
				pass