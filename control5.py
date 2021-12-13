text1 = input("Enter the string :")

text1 = text1.split()
text2 = "".join(text1)
text3 = ""
i = 0
msg = ""

while i < len(text2):
    if text2[i].isdigit():
        text3 += text2[i]
        msg = f"{text3}"
    i += 1

print("All numbers in the text :", msg)

# vladalh@mail.ru
