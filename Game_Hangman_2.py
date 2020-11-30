#The main goal here is to create a sort of “guess the word” game. The user needs to be able to input letter guesses. A limit should also be set on how many guesses they can use. This means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. No need to get too fancy.) You will also need functions to check if the user has actually inputted a single letter, to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.



print("\n\n--------------------------------------\n\
    Hello and welcome to the game. \n  You have to guess the word hidden. \n  You can guess 3 times wrong.\n  Enter 'end' to exit. Good luck, my friend! \n--------------------------------------")


word = "BANANA"


# To initially display the word in underscores
def hidden_word():
    new_word = word
    for i in range(0, len(word)):
        new_word = new_word.replace(word[i], '-')    
    return new_word
print(f"\nThis is the word in question: {hidden_word()}")


'''
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
'''

remaining_guesses = 3

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


while remaining_guesses >= 1:
    type_input()


# print(convert_letter(word))


# def apprearance_counter(user_input):
#     remaining_guesses = 5

#     # Counting appearances of input in string
#     count = word.count(user_input)

#     if remaining_guesses >= 1:
#         # Display message with letter, success and how many times
#         if count >= 1:
#             print(f"\nHooray! < {user_input.upper()} > was a match!")
#             print(f"Your letter appears {count} times.\n")

#         # Display message with fail and remaining guesses
#         elif count == 0:
#             remaining_guesses -= 1
#             print(f"That was a bad guess, no match. You have {remaining_guesses} guesses left.\n")
#         # Game over if no guesses left
#         else:
#             print("Game over...")
#             pass
