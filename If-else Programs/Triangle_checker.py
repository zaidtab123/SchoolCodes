a=float(input("Enter length of Side 1:"))
b=float(input("Enter length of Side 2:"))
c=float(input("Enter length of Side 3:"))

if a>b+c:
    if c<a+b:
        if b<a+c:
            print("It forms a triangle")
        else:
            print("It doesn't form a triangle.")
    else:
        print("It doesn't form a triangle.")
else:
    print("It doesn't form a triangle.")