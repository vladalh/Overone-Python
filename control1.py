a = input("Enter any seven-digit number :")

even_count = 0
sum_numbers = 0
msg = ""

odd_count = 0
mult = 0

for i in a:
    if int(i) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    sum_numbers += int(i)

    if even_count > odd_count:
        msg = f"Sum of all digits of the number = {sum_numbers}"
    else:
        mult = int(a[0]) * int(a[2]) * int(a[5])
        msg = f"Product of 1, 3 and 6 digits of the number = {mult}"


print(msg)

# vladalh@mail.ru