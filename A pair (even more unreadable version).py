inp = 5
item = 'item'
itemPlural = 'items'

#message = 'test'
#print(list(map(bin,bytearray(message,'utf8'))))


tf = list(True if n == '1' else False for n in bin(inp)[2:])

out = []
for v, i in zip(tf, range(len(tf))):
	out.append(len(tf) - i - 1) if v else None
	
for n, i in zip(out, range(len(out))):
	pair = f'one {item}' if i == len(out) - 1 and inp % 2 != 0 else 'a '
		
	for z in range(out[i]):
		pair += 'pair' if z < 1 else 'pairs'
		pair += ' of ' if z != out[i] - 1 else ''
	
	pair += f' of {itemPlural}' if i == len(out) - 2 or i == len(out) - 1 and inp % 2 == 0 else ''
	out[i] = pair

print(' plus '.join(out))
