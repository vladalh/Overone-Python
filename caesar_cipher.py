def ceasar_text(text: str, shift: int):
    alpha = "abcdefghijklmnoprstuqwvxyz"
    new_text = ""
    for i in text:
        if i in alpha:
            new_text += chr(ord(i) + shift)
        else:
            new_text += i
    return new_text

# The required text is entered
text = input("Enter any text:")

shift = int(input("Enter the shift amount:"))


print(ceasar_text(text, shift))

# vladalh@mail.ru
