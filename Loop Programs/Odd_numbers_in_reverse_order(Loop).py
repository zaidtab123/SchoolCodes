x=int(input("Enter lower limit: "))
y=int(input("Enter upper limit: "))
if x%2==0:
    y-=1
    for a in range(y,x,-2):
        print(a)

else:
    for a in range(y,x,-2):
        print(a)