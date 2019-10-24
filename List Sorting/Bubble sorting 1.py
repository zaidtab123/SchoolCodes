a = [13, 5, 91, 27, 36, 2]
l = len(a)
for i in range(l - 1):
    for j in range(l - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
