import random

# gets random word from list
def pick_random_word(words):
    random_word = random.choice(words).upper()

    return random_word

def get_input(): 
	# error handling
	while True:
		attempt = input("Enter a letter: \n").upper()
		if attempt.isalpha() and len(attempt) == 1:
			break
		else:
			print("{} is not a valid input. Please enter a single letter: \n".format(attempt))
			continue

	return attempt

def is_good_guess(attempt, current_word, n):
	# successful guess
	if attempt in current_word:
		return n
	# incorrect guess so increase guess count by one and output failure message	
	else:
		print("WRONG! You have {} tries left. \n".format(4-n))
		return n+1

# checks if guess matches with a letter in random word
def display_progress(current_word, attempt, progress_string):
	for index, letter in enumerate(current_word):
		if letter == attempt:
			progress_string[index] = attempt

	print(" ".join(progress_string))

# VARIABLE DEFS
words = []
progress_string = []
n=0

# import the list of words and store each as element
with open("words.txt", "r") as x:
  words_list = x.readlines()
for word in words_list:
    words.append(word.rstrip("\n"))

# picks random word and make each letter an underscore in seperate list
current_word = pick_random_word(words)
for letter in current_word:
		progress_string.append("_")

# GAME SETUP 
start_game = input("Press Enter to start \n")
print("_ "*len(current_word))

# GAME LOOP - checks for win and lose condition 
while "_" in progress_string and n<5:

	# gets attempt, changes n appropriately and then displays curent game state
	attempt = get_input()
	n = is_good_guess(attempt, current_word, n)
	display_progress(current_word, attempt, progress_string)

# win message
if "_" not in progress_string:
	print("Congratulations! You guessed the word '{}' correctly\n".format(current_word))

# loss message
if n==5:
	print("That's your last guess! Better luck next time. The word was '{}'\n".format(current_word))








