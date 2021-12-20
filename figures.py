import math


a = float(input("Enter the length of side A in cm:"))
b = float(input("Enter the length of side B in cm:"))
c = float(input(("Enter the length of side C in cm:")))

p1 = (a + b + c) / 2  # perimeter_of_a_triangle

s1 = (p1 * (p1 - a) * (p1 - b) * (p1 - c)) ** 0.5  # calculating the area of a triangle

x1 = float(input("Enter the length of the side of the square in cm:"))

p2 = 4 * x1  # Calculating the perimeter of a square
s2 = x1 ** 2  # Calculating the area of a square

r1 = float(input("Enter the radius of the circle in cm:"))

p3 = 2 * math.pi * r1 # Calculating the perimeter of a circle
s3 = math.pi * (r1 ** 2) # Calculating the area of a circle

r2 = float(input("Enter the radius of the sphere in cm:"))

s4 = 4 * math.pi * (r2 ** 2)  # Calculating the surface area of a sphere
v1 = (4 / 3) * math.pi * (r2 ** 3) # Calculating the volume of a sphere

x2 = float(input("Enter the length of the side of the edge of the cube in cm:"))

s5 = 6 * (x2 ** 2)  # Calculating the surface area of a cube
v2 = x2 ** 3  # Calculating the volume of a cube
sqr = s1 + s2 + s3 + s4 + s5  # calculating the total area of all shapes

print("The perimeter and area of the triangle are respectively :", '{0:.2f}'.format(p1), "cm",
      "and", '{0:.2f}'.format(s1), "sq.cm")

print("The perimeter and area of the square are equal respectively :", '{0:.2f}'.format(p2), "cm",
      "and", '{0:.2f}'.format(s2), "sq.cm")

print("The perimeter and area of the circle are equal respectively :", '{0:.2f}'.format(p3), "cm",
      "and", '{0:.2f}'.format(s2), "sq.cm")

print("The area and volume of the sphere are equal respectively :", '{0:.2f}'.format(s4), "sq.cm",
      "and", '{0:.2f}'.format(v1), "cubic cm")

print("The area and volume of the cube are equal respectively :", '{0:.2f}'.format(s5), "sq.cm",
      "and", '{0:.2f}'.format(v2), "cubic cm")

print("the total area of all figures is :", '{0:.2f}'.format(sqr), "sq.cm")

#vladalh@mail.ru
