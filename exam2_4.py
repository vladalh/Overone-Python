list1 = "An apple a day keeps the doctor away"

letter_dict = {}
count_letter = 0

for let in list1:
    letter_dict[let] = list1.count(let)

print(letter_dict)
