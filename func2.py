def foo(x):
    x = [3, 2, 1]

def foo1(x):
    x[0] = 0

arr = [1, 2, 3]
foo(arr)
print(arr)
foo1(arr)
print(arr)