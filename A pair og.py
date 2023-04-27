inp = 11
item = 'item'
itemPlural = 'items'
#message = 'test'
#print(list(map(bin,bytearray(message,'utf8'))))

bin = bin(inp)[2:]
print(bin)#debug

#tf = list(map(lambda n : True if n == '1' else False, bin)) #is this faster or slower?
tf = list(True if n == '1' else False for n in bin)

out = []
for v, i in zip(tf, range(len(tf))):
	if v:
		out.append(len(tf) - i - 1)
	
for n, i in zip(out, range(len(out))):
	if i == len(out) - 1 and inp % 2 != 0:
		pair = f'one {item}'
	else:	
		pair = 'a '
		
	for z in range(out[i]):
		pair += 'pair' if z < 1 else 'pairs'
		if z != out[i] - 1:
			pair += ' of '
	
	if i == len(out) - 2 or i == len(out) - 1 and inp % 2 == 0:
		pair += f' of {itemPlural}'
	out[i] = pair

print(out)	
print(' plus '.join(out))
