import linecache
import sys
from states import *
from random import randint
from control import *
# Create the needed new word

word = list(linecache.getline(
    ('../resources/words.txt'), randint(1, 55900)).strip())
slot = list('_' * len(word))
hanged = 0

############################################################
# Here they end the static values, and now we will compare #
############################################################

def punish():
    global statedict
    hanged += 1
    print(statedict[hanged])


def destiny(a):
    for i in range(len(word)):
        if a == word[i]:
            slot[i] = a
        else:
            punish()

    print(''.join(slot))


def main():
    while word != slot:
        a = input("$: ")
        valid(a)
        if valid(a) == True:
            destiny(a)
        else:
            print("you should provide a single letter")
    else:
        print("you have won!")
        sys.exit(0)


main()
