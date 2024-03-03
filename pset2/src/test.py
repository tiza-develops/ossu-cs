state = 0
def punish():
	global state
	hanged = state
	hanged += 1
	state = hanged
	print(state)
punish()
