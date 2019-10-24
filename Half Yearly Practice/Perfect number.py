a = int(input('Enter a number: '))
s = 0
for i in range(1, a):
    if a % i == 0:
        s += i

if s == a:
    print(a, 'is a perfect number.')
else:
    print(a, 'is not a perfect number.')

