for i in range(4):
    for j in range(7):
        if j == 0 or j == 4:
            if i == 0:
                print(' ', end='')

            else:
                print('*', end='')
        else:
            if i == 0:
                print('*', end='')

            else:
                print(' ', end='')
    print()