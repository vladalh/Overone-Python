def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "The figure is a triangle"
    else:
        return "The shape is not a triangle"


# the user enters the lengths of the sides

a = float(input("Enter side A :"))
b = float(input("Enter side B :"))
c = float(input("Enter side C :"))


print(triangle(a, b, c))

# vladalh@mail.ru