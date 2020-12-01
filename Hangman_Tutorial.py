import random
from words import word_list


def get_word():
	word = random.choice(word_list)
	print(word.upper())
	return word.upper()


def play(word):
	word_completion = "_" * len(word)
	guessed = False
	guessed_letters = []
	guessed_words = []
	tries = 6

	print("Let's play Hangman!")
	print(f"Remaining guesses: {tries}")
	print(word_completion)
	print("\n")

	while not guessed and tries > 0:
		print(f"Your guessed letters so far: {guessed_letters}")
		guess = input("Please guess a letter: ").upper()
		#guess = "A"
		if len(guess) == 1 and guess.isalpha():
			if guess in guessed_letters:
				print("You already guessed that one!", guess)
			elif guess not in word: 
				tries -= 1
				print(f"{guess} is not in the word! Remaining guesses: {tries}")
				guessed_letters.append(guess)
			else:
				print(f"\nMatch! {guess} is in the word!\n")
				guessed_letters.append(guess)
				word_as_list = list(word_completion)
				word_as_list = [letter if letter in guessed_letters else '_' for letter in word]
				# indices = [i for i, letter in enumerate(word) if letter == guess]
				# for index in indices:
				# 	word_as_list[index] = guessed_letters

				word_as_list = list(map(''.join, word_as_list))
				word_completion = ''.join(word_as_list)
				print(word_completion, "\n")

				if "_" not in word_completion:
					guessed = True
		else:
			print("Not a valid guess :-(")


	# print(tries)
	# print(word_completion)
	# print("\n")

	if guessed == True:
		print(f"\n----------------------\nCongrats, you did it. You guessed the word {word}.\n----------------------\n")
	elif tries < 1: 
		print(f"\n----------------------\nAwwwww, you ran out of tries. The word was: {word}.\n----------------------\n")


def main():
	word = get_word()
	play(word)

main()









