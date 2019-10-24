x=[10,20,10,20,40,40,40,10,30,40,50,60]
l=len(x)
p=int(input('Enter the element whose frequency u want to find: '))
f=0

for i in range(l):
    
    if x[i]==p:
        f+=1
if f==0:
    print('The element doesn\'t exit in the list')
else:
    print('The frequency of element',p,'is',f)
    
