n=int(input("Enter the number of inputs: "))
small=None
x=int(input("Enter the number: "))
small=x

for b in range(n-1):
    a=int(input("Enter the number: "))
    
    if a<small:
        small=a
        
        
print(small,"is the smallest number.")
