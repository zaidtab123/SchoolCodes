n=int(input("Enter the number of inputs: "))
big=None
x=int(input("Enter the number: "))
big=x

for b in range(n-1):
    a=int(input("Enter the number: "))
    
    if a>big:
        big=a
        
        
print(big,"is the biggest number.")
