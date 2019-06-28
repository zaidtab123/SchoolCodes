x=int(input("Enter the year: "))

if x%4==0 and x%100!=0:
    print(x,"is a leap year.")
    
elif x%400==0 and x%100==0:
    print(x,"is a leap year.")
    
else:
    print(x,"is not a leap year.")