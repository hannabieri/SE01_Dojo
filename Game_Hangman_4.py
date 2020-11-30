game_active = True

# To initially display the word in underscores
def hidden_word():
    new_word = word
    for i in range(0, len(word)):
        new_word = new_word.replace(word[i], '-')    
    return new_word


# To check later on and replace underscores with letter
def iterate_hidden(letter_passed):
    underscores = hidden_word()
    print(f"Here underscores {underscores}")
    new_word = word
    for i in range(0, len(word)):
        if letter_passed == word[i]:
            # Determine position (index) of letters to replace underscore
            position_letters = [pos for pos, char in enumerate(new_word) if char == word[i]]
            print(position_letters)
            # Replace underscores with passed letter
            for position_letter in position_letters:
                underscores = underscores[:position_letter] + letter_passed + underscores[position_letter+1:]
    return underscores


# Main function
def type_input():
    global remaining_guesses
    input_letter = input("\nWhich letter do you guess? Answer here: ")
    #input_letter = "a" 

    # Checks if input is valid
    if len(input_letter) == 1:
        input_letter = input_letter.upper()    

        if input_letter in word:
            # Counting appearances of input in string
            count = word.count(input_letter)
            print(f"\nIt's a match! Your letter {input_letter} appears {count} times.\n")
            return word
            # Call function to change displaying of word
            #print("This is the word in question: ", iterate_hidden(input_letter))
        
        elif (input_letter not in word):
            remaining_guesses -= 1
            print(f"That was a bad guess :-(. You have {remaining_guesses} guesses left.\n")
            # Game over if no guesses left
            if remaining_guesses == 0:
                print("\n\n--------------------------\nGame over...")
                user_input = input("Want to play again? Enter yes (y) or no (n)! \n--------------------------\n")
                # Check if user wants to play again
                if user_input.lower() == "y":
                    return type_input()
                else:
                    print("Ok, see you another time!\n")
                    return

            return remaining_guesses


    # Checks if input is invalid
    else: 
        print("\nLooks like an invalid input! Try again.")
        return type_input() 


def play_game():
	while remaining_guesses >= 1:
    type_input()








word = "BANANA"
remaining_guesses = 3

print("\n\n--------------------------------------\n\
    Hello and welcome to the game. \n  You have to guess the word hidden. \n  You can guess 3 times wrong.\n  Enter 'end' to exit. Good luck, my friend! \n--------------------------------------")
print(f"\nThis is the word in question: {hidden_word()}")

play_game()











