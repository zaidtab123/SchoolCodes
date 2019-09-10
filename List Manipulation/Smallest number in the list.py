p=[10,20,15]
l=len(p)
small=p[0]
index=0

for i in range(1,l):
    if p[i]<small:
        small=p[i]
        index=i
        

print("The smallest number is",small,'and it\'s index is',index)
