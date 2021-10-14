
b='AUPEZH '
for i in range(0,len(b)):
   if ord(b[i]) in range(65,90):
      b=b.replace(b[i],chr(ord(b[i])+1))
for i in range(0,len(b)):      
   if ord(b[i])==90:
       b=b.replace(b[i],'A')
   if ord(b[i])==32:
       b=b.replace(b[i],'-')
print(b)
     