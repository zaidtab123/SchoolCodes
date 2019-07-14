x=int(input("Enter the number the products you are buying: "))
if x<10 and x>0:
    print("Final amount is: Rs.", x*120)
elif x>=10 and x<=99:
    print("Final amount is: Rs.", x*100)
elif x>=100:
    print("Final amount is: Rs.", x*70)
else:
    print("The input is invalid!")

    