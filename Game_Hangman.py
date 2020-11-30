#The main goal here is to create a sort of “guess the word” game. The user needs to be able to input letter guesses. A limit should also be set on how many guesses they can use. This means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. No need to get too fancy.) You will also need functions to check if the user has actually inputted a single letter, to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.


print("\n\n--------------------------\n\
    Hello and welcome to the game! You have five wrong guesses in total. Good luck, my friend! \n--------------------------")

word = "BANANA"
user_input = ""




# # Replacing letters with underscores. If user input matches existing letter, do not replace it
def convert_letter(word):
    new_word = word
    for i in range(0, len(word)):
        if input_letter == word[i]:
            pass
        else: 
            new_word = new_word.replace(word[i], '_ ')
    return new_word



def type_input(input_letter):
    # input_letter = "n"
    input_letter = input("\nWhich letter do you guess? Answer here: ")
    if len(input_letter) > 1:
        print("\nLooks like an invalid input! Try again.")
        type_input(input_letter)
    else: 
        print("\ninput valid")
        input_letter = input_letter.upper()    
        # apprearance_counter(user_input)
        return convert_letter(input_letter)
        # return input_letter

user_input = type_input(user_input)



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



# print(convert_letter(word))
# print(input_check(user_input))
# print(apprearance_counter(user_input))