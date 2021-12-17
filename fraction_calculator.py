import math

def calculating_fractions(x1, x2, y1, y2, sign):
    devisor = math.gcd(x2, y2)
    if sign == '+':
        if y1 == y2:
            num = x1 + x2
            denom = y1
        else:
            num = (x1 * y2) + (x2 * y1)
            denom = y1 * y2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    elif sign == '-':
        if y1 == y2:
            num = x1 - x2
            denom = y1
        else:
            num = (x1 * y2) - (x2 * y1)
            denom = y1 * y2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    elif sign == '*':
        num = x1 * x2
        denom = y1 * y2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    elif sign == '/':
        num = x1 * y2
        denom = y1 * x2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    if num < denom:
        return result
    else:
        return  f"{int(num // denom)} {int((num % denom) // devisor)}/{int((denom) // devisor)}"


numerator1 = int(input("Enter the numerator1 :"))
denominator1 = int(input("Enter the denominator :"))
operator = input("Enter operator +, -, *, / :")
numerator2 = int(input("Enter the numerator2 :"))
denominator2 = int(input("Enter the denominator :"))

print(calculating_fractions(numerator1, numerator2, denominator1, denominator2, operator))

# vladalh@mail.ru
