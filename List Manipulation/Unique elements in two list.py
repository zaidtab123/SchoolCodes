a = []
b = []
c = a + b
u = []
siz = int(input('Enter the number of elements required in the list: '))
for i in range(siz):
    x = int(input('\nEnter the element to be inserted in list 1: '))
    y = int(input('Enter the element to be inserted in list 2: '))
    a.append(x)
    b.append(y)
for p in range(len(c)):
    x = c[i]
    if x in a and x not in b:
        u.append(x)
    elif x in b and x not in a:
        u.append(x)
print('Unique list=', u)
