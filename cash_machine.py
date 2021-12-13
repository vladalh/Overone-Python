cash = float(input("Enter the price of the product in the format rub.kop :"))

end_price = 0

while cash > 0:
    end_price += float(cash) * 100
    cash = float(input("Enter the price of the product in the format rub.kop :"))
print("total amount:", int(end_price // 100), "roubles", int(end_price % 100), "kopecks")

# vladalh@mail.ru
