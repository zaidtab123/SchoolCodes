x = int(input('Enter the number: '))
y = 1

for i in range(6):
    if x >= 500:
        y = x // 500
        x = x - (500 * y)
        print('500 *', y)

    elif x >= 200 and x <= 500:
        y = x // 200
        x = x - (200 * y)
        print('200 *', y)

    elif x >= 100 and x <= 200:
        y = x // 100
        x = x - (100 * y)
        print('100 *', y)

    elif x >= 10 and x <= 100:
        y = x // 10
        x = x - (10 * y)
        print('10 *', y)

    else:
        if x == 0:
            break
        else:
            print('1 *', x)