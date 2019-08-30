x = [20, 15, 2, 3, 5, 7, 2, 10, 5, 30, 5, 60, 17, 11, 18, 2, 5, 3, 2, 2, 8]
a = 0
unique = []
repeat = []

for i in range(len(x)):
    c = x.count(x[i])
    if c == 1:
        unique.append(x[i])

    else:
        repeat.append(x[i])

print('Unique elements=', unique)

repeat1 = list(dict.fromkeys(repeat))

for z in repeat1:
    c = repeat.count(repeat1[a])
    print(z, 'is repeated', c, 'times')
    a += 1
