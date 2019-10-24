x = int(input('Enter the units used: '))
t = 0

if x <= 50:
    t = x * 0.5

elif x > 50 and x <= 150:
    t = (50) * 0.5
    x -= 50
    t = t + (x * 0.75)

elif x > 150 and x <= 250:
    t = 50 * 0.5
    x -= 50
    t = t + (100 * 0.75)
    x -= 100
    t = t + (x * 1.20)

else:
    t = 50 * 0.5
    x -= 50
    t = t + (100 * 0.75)
    x -= 100
    t = t + (100 * 1.20)
    x -= 250
    t = t + (x * 1.5)

f = t + (0.2 * t)
print('Amount to be paid is Rs.', f)

