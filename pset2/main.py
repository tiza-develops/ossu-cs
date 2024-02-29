import linecache
import itertools
from random import randint
from states import *
from validate import *

# Create the needed new word 
word = list(linecache.getline(('words.txt'), randint(1, 55900)).strip())
slot = list('_' * len(word))
hanged = state0
############################################################
# Here they end the static values, and now we will compare #
############################################################

def guess():
	guess = input("Please enter a letter: ")
	if valid(guess) == True:
		return guess
	else:
		return print("you need to enter a single case letter")

def destiny():
	lucky = guess()
	for l in range(len(word)):
		if lucky == word[l]:
			slot[l] == lucky
		else:
			pass
	print(slot)

def main():
	while list(slot) != word:
		destiny()
	else:
		print("yay, you have won :)")

main()

