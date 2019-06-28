git remote add origin https://github.com/zaidtab123/py.codes-C.S.Academy.git
git push -u origin master
p=round((float(input("Enter the principal amount: "))),2)
r=round((float(input("Enter the rate of interest: "))),2)
t=round((float(input("Enter the number of years: "))),2)
n=round((float(input("Enter the number of times in a year the interest gets compounded: "))),2)
si=(p*r*t)/100
ci=p*(1/r*t)**(n*t)
print("Simple Interest=", si, "\nCompound Interest=",round(ci,2))