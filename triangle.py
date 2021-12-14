# the user enters the lengths of the sides

a = float(input("Enter side A :"))
b = float(input("Enter side B :"))
c = float(input("Enter side C :"))

# determine if a shape with the specified sides is a triangle
if a + b > c and a + c > b and b + c > a:
    print("The figure is a triangle")
else:
    print("The shape is not a triangle")

# vladalh@mail.ru