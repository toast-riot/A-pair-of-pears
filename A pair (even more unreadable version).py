#This is as unreadable as I could make it without using semicolons
inp,item,itemPlural=5,'item','items'
s,d,r=inp,item,itemPlural
f=list(True if n=='1'else False for n in bin(s)[2:])
o=[]
for v,i in zip(f,range(len(f))):
 o.append(len(f)-i-1)if v else None
for n,i in zip(o,range(len(o))):
 p=f'one {d}'if i==len(o)-1and s%2!=0 else'a '
 for z in range(o[i]):
  p+='pair'if z<1else'pairs'
  p+=' of 'if z!=o[i]-1else''
 p+=f' of {r}'if i==len(o)-2or i==len(o)-1and s%2==0else''
 o[i]=p
print(' plus '.join(o))
