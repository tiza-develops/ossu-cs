import linecache
import itertools
from random import randint
from states import *
from validate import *

# Create the needed new word 
word = list(linecache.getline(('words.txt'), randint(1, 55900)).strip())
slot = '_' * len(word)
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
	for (i,j) in zip(word,slot):
		if lucky == i:
			slot[j] == lucky
		else:
			pass

def main():
	destiny()

main()
