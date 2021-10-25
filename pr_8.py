b='AUPEZH '
c=b
d=b
for i in range(0,len(b)):
   if ord(b[i]) in range(65,90):
      c=c.replace(b[i],chr(ord(b[i])+1))
print(c)
for i in range(0,len(b)):      
   if ord(b[i])==90:
       b=b.replace(b[i],'A')
   if ord(b[i])==32:
       d=d.replace(b[i],'-')
print(b)
print(d)