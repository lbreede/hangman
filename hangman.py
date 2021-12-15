import random
from collections import Counter

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WORDS = {"DOG", "CAT", "RABBIT", "COW", "RAVEN", "DEER", "SAMOYED", "HORSE"}
WPAD = "   "
LPAD = "   "
ERROR = "TRY AGAIN: "

def guess_letter(word, correct, incorrect):
	guess = input(f"{LPAD}Guess a letter: ")
	guess = guess.upper()

	if len(guess) > 1:
		print(f"{LPAD}{ERROR}Too many characters in guess {guess}\n")
		return False

	if guess not in ALPHABET:
		print(f"{LPAD}{ERROR}{guess} is not an acceptable guess!\n")
		return False

	word = word.upper()

	if guess not in correct and guess not in incorrect:
		if guess in word:
			correct.add(guess)
		else:
			incorrect.add(guess)
		return True

	else:
		print(f"{LPAD}{ERROR}You've already guessed {guess}!\n")
		return False

def print_alphabet(correct, incorrect):
	line1 = ""
	line2 = ""

	for letter in ALPHABET[:13]:
		if letter in correct or letter in incorrect:
			letter = "."
		line1 += letter + WPAD

	for letter in ALPHABET[13:]:
		if letter in correct or letter in incorrect:
			letter = "."
		line2 += letter + WPAD

	print()
	print(LPAD + line1)
	print(LPAD + line2)
	print()

def print_hangman(incorrect):
	with open("hangman.txt", "r") as f:
		lines = [x.split(" ") for x in f.read().split("\n")]

	idx = len(incorrect)
	print(LPAD + lines[0][idx])
	print(LPAD + lines[1][idx])
	print(LPAD + lines[2][idx])
	print(LPAD + lines[3][idx])
	print(LPAD + lines[4][idx])
	print(LPAD + lines[5][idx])
	print(LPAD + lines[6][idx])
	print()
	return idx

def print_word(word, correct):
	word = word.upper()
	hidden_word = ""
	for letter in word:
		if letter not in correct:
			letter = "_"

		hidden_word += letter + WPAD

	print(LPAD + hidden_word)
	print()

def main():
	c = set()
	i = set()
	w = random.sample(WORDS, 1)[0]

	print_alphabet(c, i)
	attempt = print_hangman(i)
	print_word(w, c)

	while True:

		if guess_letter(w, c, i):
			print_alphabet(c, i)
			attempt = print_hangman(i)
			print_word(w, c)

			if attempt == 6:
				print(f"{LPAD}You lost!")
				break

			elif Counter(c) == Counter(set(w.upper())):
				print(f"{LPAD}CONGRATIOLATIONS! You won!")
				break

if __name__ == '__main__':
	main()