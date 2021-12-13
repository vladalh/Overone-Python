import random

list1 = [random.randint(0, 10) for i in range(20)]
print(list1)
count_number = 0

for number1 in list1:
    for number2 in list1:
        if number1 == number2:
            count_number += 1
    count_number -= 1

result = int(count_number // 2)

print(f"The number of pairs of elements equal to each other = {result}")

