import random


a = random.randint(10, 40)
b = random.randint(10, 40)
c = random.randint(10, 40)
d = random.randint(10, 40)

print(a, b, c, d)
temp = 0
if a <= b:
    temp = a
    a = b
    b = temp


maximum = 0
print(a, b, c, d)

if a > b and a > c and a > d:
    maximum = a
elif b > c and b > d:
    maximum = b
elif c > d:
    maximum = c
else:
    maximum = d

print(maximum)
