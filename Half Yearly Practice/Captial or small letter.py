a = input('Enter the word: ')

for i in a:
    x = int(ord(i))

    if x < 90:
        print(i, 'is a Capital letter.')
    else:
        print(i, 'is a Small letter.')