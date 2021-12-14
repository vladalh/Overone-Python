import collections
import random

list1 = [random.randint(0, 10) for i in range(20)]

my_dict = dict(collections.Counter(list1))

print(my_dict)

result = 0
for key, value in my_dict.items():
    if value >= 2:
        result += value // 2

print(f"The number of pairs of elements equal to each other = {result}")
