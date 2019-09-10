x=[10,20,30,40,50,60]
l=len(x)
print(x)
p=int(input("Search: "))
index=-1

for i in range(l):
    
    if x[i]==p:
        index=i
        break;

if index!=-1:
    print('The element is found and it\'s index is',index)
    
else:
    print('This element doesn\'t exist')