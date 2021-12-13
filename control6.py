word = input("Enter a sequence of letters of different case :")

uppercase = 0  #upper
lowercase = 0  #lower
upp = 0
low = 0   # lower
sum_letter = len(word)
sum_vow = 0

for letter in word:
    if letter.islower():
        low += 1
        if low == 2:
            lowercase += 1
            low = 0
    elif letter.isupper():
        upp += 1
        if upp == 2:
            uppercase += 1
            upp = 0

    if  letter in "a, A, e, E, i, I, u, U, o, O":
        sum_vow += 1

print(f"{uppercase} uppercase pairs, {lowercase} lower case pairs")
print(f"Total letters in a word: {sum_letter}, total vowels in a word: {sum_vow}, "
      f"total consonant letters in a word: {sum_letter - sum_vow}")

# vladalh@mail.ru
