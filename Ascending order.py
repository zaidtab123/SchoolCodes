x=float(input("Enter the first number:"))
y=float(input("Enter the second number:"))
z=float(input("Enter the third number:"))
a=b=c=None
if x<y and x<z:
    if y<z:
        a,b,c=x,y,z
    else:
        a,b,c=x,z,y
        
elif x>y and y<z:
    if x<z:
        a,b,c=y,x,z
    else:
        a,b,c=y,z,x
        
else:
    if x<y:
        a,b,c=z,x,y
    else:
        a,b,c=z,y,x
        
print("Numbers in ascending orders are:",a,",",b,",",c)
    