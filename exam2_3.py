c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)

if sum(c_1) > sum(c_2):
    print(f"The amount is greater in the tuple - c_1")

else:
    print(f"The amount is greater in the tuple - c_2")

print(f"the indices of the minimum and maximum elements c_1 -: {c_1.index(min(c_1))}; {c_1.index(max(c_1))}")

print(f"the indices of the minimum and maximum elements c_2 -: {c_2.index(min(c_2))}; {c_2.index(max(c_2))}")
