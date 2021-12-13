n = int(input("Enter any number:"))

# Building a list of numbers generator
prime_numbers = [x for x in range(2, n+1) if x not in [i for sub in [list(range(2 * j, n+1, j))
    for j in range(2, n // 2)] for i in sub]]

print(*prime_numbers)

# vladalh@mail.ru
