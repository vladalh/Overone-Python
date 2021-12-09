import random

list1 = [random.randint(0, 10) for i in range(20)]
list2 = []

for number in list1:
    if list1.count(number) < 2:
        list2.append(number)

print(f"List of unique elements{list2}")