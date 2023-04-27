item = 'item'
itemPlural = 'items'

message = 'test'

encoded = []
for character in list(map(bin,bytearray(message,'utf8'))):
	character = character[2:]
	
	#tf = list(map(lambda n : True if n == '1' else False, binary)) #is this faster or slower?
	tf = list(True if n == '1' else False for n in character)
	
	out = []
	for v, i in zip(tf, range(len(tf))):
		if v:
			out.append(len(tf) - i - 1)
	
	for n, i in zip(out, range(len(out))):
		if i == len(out) - 1 and int(character[-1]) % 2 != 0:
			pair = f'one {item}'
		else:	
			pair = 'a '
			
		for z in range(out[i]):
			pair += 'pair' if z < 1 else 'pairs'
			if z != out[i] - 1:
				pair += ' of '
		
		if i == len(out) - 1 - int(character[-1]) % 2:
			pair += f' of {itemPlural}'
		out[i] = pair
	
	encoded.append(' plus '.join(out))

print(', '.join(encoded))
