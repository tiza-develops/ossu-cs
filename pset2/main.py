import linecache
from random import randint
from states import *

# Create the needed new word 
word = list(linecache.getline(('words.txt'), randint(1, 55900)).strip())
slots, slot = '_ ' * len(word) , list('_' * len(word))
hanged = state0
############################################################
# Here they end the static values, and now we will compare #
############################################################

def guess():
	input("Enter a single letter: ")

def destiny():
	lucky = guess()
	if lucky in word:
		# Print the newfound letters
	else: 
		# Punish

def main:
	if slot == word:
		print('yay, you have won')
	else:
		destiny()


