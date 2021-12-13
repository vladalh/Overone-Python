text = input("Enter any text :")

vowels = []
vowel = 0
consonants = 0

text = text.lower()
text2 = text.split(" ")
text2 = "".join(text2)

msg = ""

for i in text2:
    if i in "a, e, i, o, u":
       vowel += 1
       vowels.append(i)
    else:
       consonants += 1
       if vowel != consonants:
           msg = f"Program done"
       else:
           msg = f"All vowels in the text: , {vowels}"

print(msg)

# vladalh@mail.ru