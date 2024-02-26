from random import randint
from states import *

# Create the needed new word 
def word():
    dict = {}
    file = open("words.txt", "r")
    i = 1
    for line in file:
        line = line.strip()
        i += 1
        dict[i] = line
    w = dict[randint(1,i)]
    return w

def slots():
    hidden = word()
    slots = print('_' * len(hidden))
    return slots

############################################################
# Here they end the static values, and now we will compare #
############################################################


def validate(char):
	if len(char) == 1 and char.isalpha():
		return True
	else:
		return False
	
def search(char):
	singleton = validate(char)
	wiggy = word()
	if singleton == True:
		return wiggy.count(char)
	else:
		print("you should provide a single letter, case insensitive")

oldy = word()
current = []

def dissolve(char):
	oldy.index(char)

def main():
	slots()
	guess = input("$: ")
	search(guess)

main()

