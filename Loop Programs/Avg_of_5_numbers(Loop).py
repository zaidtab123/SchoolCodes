n=int(input("Enter the number of subjects: "))
y=0
for a in range(n):
    x=int(input("Enter mark:"))
    y+=x
    
print("The average mark is:",y/n)

