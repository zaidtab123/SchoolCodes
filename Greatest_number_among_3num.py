x=float(input("Enter the first number:"))
y=float(input("Enter the second number:"))
z=float(input("Enter the third number:"))
a=None
if x>y and x>z:
    a=x
        
elif y>x and y>z:
    a=y
        
else:
    a=z
    
print("The greatest number among them is:",a)