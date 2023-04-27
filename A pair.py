def pairify(inp, item='item', itemPlural='items'):
	inp = int(inp)
	if inp <= 0:
		return f'no pairs of {itemPlural}'
	
	binary = bin(inp)[2:]
	tf = list(True if n == '1' else False for n in binary)

	output = []
	for v, i in zip(tf, range(len(tf))):
		if v:
			output.append(len(tf) - i - 1)
		
	for i in range(len(output)):
		if i == len(output) - 1 and inp % 2 != 0:
			pair = f'one {item}'
		else:	
			pair = 'a '
			
		for z in range(output[i]):
			pair += 'pair' if z < 1 else 'pairs'
			if z != output[i] - 1:
				pair += ' of '
				
		if i == len(output) - 1 - inp % 2:
			pair += f' of {itemPlural}'
		output[i] = pair

	return(' plus '.join(output))


print('You have ' + pairify(input('How many pears do you have? >> '), 'pear', 'pears') + '.')