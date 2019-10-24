x = input('Enter a number: ')
s = 0
for i in x:
    a = int(i)
    s += (i ** 3)

if s == x:
    print(x, 'is a armstrong number.')

else:
    print(x, 'is NOT a armstrong number.')
