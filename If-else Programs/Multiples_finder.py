print("Enter 5 numbers below")
a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
c= float(input("Enter the third number: "))
d= float(input("Enter the fourth number: "))
e= float(input("Enter the fifth number: "))

div= float(input("Enter the divisor: "))
count=0
rem= a%div
if rem==0:
    print(a, sep=' ')
    count+=1
    
rem= b%div
if rem==0:
    print(b, sep=' ')
    count+=1
    
rem= c%div
if rem==0:
    print(c, sep=' ')
    count+=1
    
rem= d%div
if rem==0:
    print(d, sep=' ')
    count+=1
    
rem= e%div
if rem==0:
    print(e, sep=' ')
    count+=1

print(count,"multiples of",div,"found")
