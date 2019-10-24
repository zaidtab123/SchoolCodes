a = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
b = ((10, 11, 12), (13, 14, 15), (16, 17, 18))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] + b[i][j], end=' ')
    print()