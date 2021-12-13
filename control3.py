import random

iter_4th_random_number_1 = 0
iter_4th_random_number_2 = 0
sum_a_b = 0
sum_rand = 0
i = 0
msg = ""

for i in range(7):

    a = int(input("Enter any number A from 1 to 20 :"))
    b = int(input("Enter any number B from 1 to 20 :"))

    random_1 = random.randint(1, 20)
    random_2 = random.randint(1, 20)

    if (a + b) > (random_1 + random_2):
        sum_a_b += 1
    else:
        sum_rand += 1

    if i == 4:
        iter_4th_random_number_1 = random_1
        iter_4th_random_number_2 = random_2

    i += 1

if sum_a_b == sum_rand:
    msg = f"4th iteration random number : {iter_4th_random_number_1 = } {iter_4th_random_number_2 = }"
else:
    msg = f"The entered pair of numbers is more than {sum_a_b} times"

print(msg)
