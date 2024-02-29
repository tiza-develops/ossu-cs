string = list('lmfao')
hidden = list('_' * len(string))

while hidden != string:
	m = input("$: ")

	for i in range(len(string)):
		if m == string[i]:
			hidden[i] = m
		else: 
			continue

	print(hidden)
else:
	print('yay')
