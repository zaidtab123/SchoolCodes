x = list(input('Enter a list: '))
for i in range(5):
    y = int(input('Enter a number: '))
    x.append(y)
    s = 0
    for z in x:
        z = int(z)
        s += z
    print(s)