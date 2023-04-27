#This is as squished and unreadable as I could make it without using semicolons, backslashes or exec()
#Config (spared from the unreadable-ness)
inp = 5
item = 'item'
itemPlural = 'items'

s,d,r,q,l,x,u,o=inp,item,itemPlural,range,len,zip,None,[]
f=list(True if n=='1'else False for n in bin(s)[2:])
for v,i in x(f,q(l(f))):
 o.append(l(f)-i-1)if v else u
for n,i in x(o,q(l(o))):
 p=f'one {d}'if i==l(o)-1and s%2!=0 else'a '
 for z in q(o[i]):
  p+='pair'if z<1else'pairs'
  p+=' of 'if z!=o[i]-1else''
 p+=f' of {r}'if i==l(o)-1-s%2!=0else''
 o[i]=p
print(' plus '.join(o))
