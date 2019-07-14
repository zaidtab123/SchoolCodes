x= int(input("Enter your age: "))
y= input("Enter your gender:")

if x>=18:
    if y=="male" or y=="Male" or y=="M" or y=="m":
        print("The candidate is male and is eligable to vote.")
        
    elif y=="female" or y=="Female" or y=="F" or y=="f":
        print("The candidate is female and is eligable to vote.")
        
    else:
        print("Invalid input!!!")
        
elif x<18:
    print("The candidate is not eligable to vote.")
    
else:
    print("Invalid Age!!!")