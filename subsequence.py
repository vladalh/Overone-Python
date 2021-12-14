import random

# create a list of 10 random numbers
number = [random.randint(-100, 100) for i in range(10)]

# making lists of even and odd numbers
even = []
odd = []

# making lists of positive and negative numbers
positive = []
negative = []


# fill in lists of even and odd numbers
for x in number:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)


# fill in lists of positive and negative numbers
for x in number:
    if x < 0:
        negative.append(x)
    else:
        positive.append(x)


print(number)
print(len(even))
print(len(odd))
print(len(positive))
print(len(negative))
print(min(positive))
print(max(negative))

# vladalh@mail.ru
