n = int(input('Enter the n value: '))
x = int(input('Enter the x value: '))
a = 1

for i in range(1, n+1):
    z = 1 / (i * x)
    a += z

a = round(a, 3)
print('The answer is:', a)
