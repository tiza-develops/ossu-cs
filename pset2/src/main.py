import linecache
from random import randint
from control import *

# Create the needed new word 

word = list(linecache.getline(('../resources/words.txt'), randint(1, 55900)).strip())
slot = list('_' * len(word))

############################################################
# Here they end the static values, and now we will compare #
############################################################

def main():
	while word != slot:
		a = input("$: ")
		valid(a)
		if valid(a) == True:
			for i in range(len(word)):
				if a == word[i]:
					slot[i] = a
				else:
					pass         
			print(''.join(slot))
		else:
			print("you should provide a single letter")

main()
