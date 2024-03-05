state0 = 0
state1 = 1
state2 = 2
state3 = 3
state4 = 4

def punish():
	global state
	hanged = state
	hanged += 1
	state = hanged
	print(state)
punish()
