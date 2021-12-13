import ast

# Enter any integer
a = int(input("Enter an integer :"))
print(a, type(a))

# Converting a number to a string
s = repr(a)
print(s, type(s))

# Converting a string to a number
a1 = ast.literal_eval(s)
print(a1, type(a1))

#vladalh@mail.ru
