def zodiac(day, mohth):
    if (day >= 21 and month == 3) or (1 <= day <= 19 and month == 4):
        return "Zodiac sign: Aries"
    elif (day >= 20 and month == 4) or (1 <= day <= 20 and month == 5):
        return "Zodiac sign: Taurus"
    elif (day >= 21 and month == 5) or (1 <= day <= 21 and month == 6):
        return "Zodiac sign: Gemini"
    elif (day >= 22 and month == 6) or (1 <= day <= 22 and month == 7):
        return "Zodiac sign: Cancer"
    elif (day >= 23 and month == 7) or (1 <= day <= 22 and month == 8):
        return "Zodiac sign: Leo"
    elif (day >= 23 and month == 8) or (1 <= day <= 22 and month == 9):
        return "Zodiac sign: Virgo"
    elif (day >= 23 and month == 9) or (1 <= day <= 23 and month == 10):
        return "Zodiac sign: Libra"
    elif (day >= 24 and month == 10) or (1 <= day <= 22 and month == 11):
        return "Zodiac sign: scorpio"
    elif (day >= 23 and month == 11) or (1 <= day <= 21 and month == 12):
        return "Zodiac sign: Sagittarius"
    elif (day >= 22 and month == 12) or (1 <= day <= 20 and month == 1):
        return "Zodiac sign: Capricorn"
    elif (day >= 21 and month == 1) or (1 <= day <= 18 and month == 2):
        return "Zodiac sign: Aquarius"
    elif (day >= 19 and month == 2) or (1 <= day <= 20 and month == 3):
        return "Zodiac sign: Pisces"



day = int(input("Enter birthday :"))
month = int(input("Enter the month of birth :"))

print(zodiac(day, month))

# vladalh@mail.ru
