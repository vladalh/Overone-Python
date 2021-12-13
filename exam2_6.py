import random

list1 = [random.randint(0, 50) for i in range(20)]
list2 = [random.randint(0, 50) for j in range(20)]

sum_count = 0

for number in list1:
    if number in list2:
        sum_count += 1

print(f"The two lists simultaneously include : {sum_count}")

