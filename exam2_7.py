import random

try:
    x = random.randint(0, 100)
    y = random.randint(0, 100)

    z = x / y

    print("The division result is : {0:.3f}".format(z))

except ZeroDivisionError:
    print(f"You cannot divide by zero")

finally:
    print(f"The program has terminated")
