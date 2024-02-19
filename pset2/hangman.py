from random import randint

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

state0 = """

   |-----------|
   |           |
   |            
   |
   |
   |
 _____
        """

state1 = """

   |-----------|
   |           ◯
   |            
   |
   |
   |
 _____
         """

state2 = """
   |-----------|
   |           ◯
   |           | 
   |
   |
   |
 _____

         """

state3 = """
   |-----------|
   |           ◯
   |          /| 
   |
   |
   |
 _____

         """

state4 = """
   |-----------|
   |           ◯
   |          /|\ 
   |
   |
   |
 _____

         """

state5 = """
   |-----------|
   |           ◯
   |          /|\ 
   |          /
   |
   |
 _____


         """

def hanged():
    state = 0
    """
    if correct:
        state += 1
    else:
        pass
    """

def main():
    guess = input("$: ")

print(state0)
