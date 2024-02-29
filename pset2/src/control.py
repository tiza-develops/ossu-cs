import sys

def valid(a):
	if len(a) == 1 and a.isalpha():
		return True
	elif a == "quit()":
		sys.exit(0)
	else:
		return False
