p=[10,20,15]
l=len(p)
big=p[0]
index=0

for i in range(1,l):
    if p[i]>big:
        big=p[i]
        index=i
        

print("The biggest number is",big,'and it\'s index is',index)
