print("Sum of odd or even from first n natural number.")

x=int(input("Enter the 'n' value: "))

sum1=0
for a in range(1,x,2):
     sum1+=a
print("Sum of first odd number is:",sum1)
     
sum2=0
for a in range(2,x,2):
    sum2+=a
print("Sum of first even number is:",sum2)

