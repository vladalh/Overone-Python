import math

numerator1 = int(input("Enter the numerator1 :"))
denominator1 = int(input("Enter the denominator :"))
operator = input("Enter operator +, -, *, / :")
numerator2 = int(input("Enter the numerator2 :"))
denominator2 = int(input("Enter the denominator :"))

result = ""

if operator == "+":
    numerator3 = (numerator1 * denominator2) + (numerator2 * denominator1)
    denominator3 = denominator1 * denominator2
    divisor = math.gcd(numerator3, denominator3)

    if numerator3 > denominator3:
        whole = numerator3 // denominator3
        result = f"{int(whole)} {int((numerator3 % denominator3) // divisor) }/{int(denominator3 // divisor)}"
    else:
        result = f"{int(numerator3 // divisor)}/{int(denominator3 // divisor)}"

elif operator == "-":
    numerator3 = (numerator1 * denominator2) - (numerator2 * denominator1)
    denominator3 = denominator1 * denominator2
    divisor = math.gcd(numerator3, denominator3)

    if numerator3 > denominator3:
        whole = numerator3 // denominator3
        result = f"{int(whole)} {int((numerator3 % denominator3) // divisor) }/{int(denominator3 // divisor)}"
    else:
        result = f"{int(numerator3 // divisor)}/{int(denominator3 // divisor)}"

elif operator == "*":
    numerator3 = numerator1 * numerator2
    denominator3 = denominator1 * denominator2
    divisor = math.gcd(numerator3, denominator3)

    if numerator3 > denominator3:
        whole = numerator3 // denominator3
        result = f"{int(whole)} {int((numerator3 % denominator3) // divisor) }/{int(denominator3 // divisor)}"
    else:
        result = f"{int(numerator3 // divisor)}/{int(denominator3 // divisor)}"

elif operator == "/":
    numerator3 = numerator1 * denominator2
    denominator3 = denominator1 * numerator2
    divisor = math.gcd(numerator3, denominator3)

    if numerator3 > denominator3:
        whole = numerator3 // denominator3
        result = f"{int(whole)} {int((numerator3 % denominator3) // divisor) }/{int(denominator3 // divisor)}"
    else:
        result = f"{int(numerator3 // divisor)}/{int(denominator3 // divisor)}"

print(result)

# vladalh@mail.ru