s1 = float(input("Enter the marks of subject 1:"))
s2 = float(input("Enter the marks of subject 2:"))
s3 = float(input("Enter the marks of subject 3:"))
s4 = float(input("Enter the marks of subject 4:"))
s5 = float(input("Enter the marks of subject 5:"))
avg = (s1 + s2 + s3 + s4 + s5) / 5
print("Your average mark is", avg)
if avg > 90 and avg <= 100:
    print('Your grade is A')
elif avg > 80 and avg <= 90:
    print('Your grade is B')
elif avg > 70 and avg <= 80:
    print('Your grade is C')
elif avg > 60 and avg <= 70:
    print('Your grade is D')
elif avg > 50 and avg <= 60:
    print('Your grade is E')
else:
    print('Fail! Better luck next time.')
