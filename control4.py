import random

num_of_ent_numbers = int(input("Enter the number of numbers to enter :"))
required_digit = int(input("Enter the number you are looking for :"))

summ_digit = 0
str_numbers = ""

i = 0

while i < num_of_ent_numbers:

    rand_number = random.randint(0, 20)
    str_numbers += f"{str(rand_number)}"
    i += 1

print(str_numbers)
print(f"The desired digit has been encountered {str_numbers.count(str(required_digit))} time(s)")

# vladalh@mail.ru
