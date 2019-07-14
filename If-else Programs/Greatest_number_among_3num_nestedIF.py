x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
z=float(input("Enter the third number: "))

if x>y:
    if x>z:
        print(x,"is the biggest number.")
        
    else:
        print(z,"is the largest number.")
        
else:
    if y>z:
        print(y,"is the biggest number.")
        
    else:
        print(z,"is the biggest number.")