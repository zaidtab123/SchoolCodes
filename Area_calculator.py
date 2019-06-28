def triangle():
    b=float(input("Enter the length of the base: "))
    h=float(input("Enter the height of the triangle: "))
    area=0.5*b*h
    print("Area of the triangle is: ",area)
    
def circle():
    r=float(input("Enter the radius: "))
    area=(3.14)*(r**2)
    print("Area of the circle is: ",area)
    
def square():
    s=float(input("Enter the length of the side: "))
    area=s**2
    print("Area of the square is: ",area)

print("Area Calculator \n1.Triangle \n2.Circle \n3. Square")
x=int(input("\nEnter your choice:"))

if x==1:
    triangle()

elif x==2:
    circle()

elif x==3:
    square()

else:
    print("Not accepted! Enter a valid number!")

#In Experiment Branch
