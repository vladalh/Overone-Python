confectionery_dict = {"торт": ["состав - мука, сахар, дрожжи, арахис, шоколад, заварной крем",
                               "цена за 100 гр - ", 1.95, "руб", "вес - ", 3900, "гр"],
                      "пироженое": ["состав - мука, сахар, грецкий орех, разрыхлитель",
                                    "цена за 100 гр - ", 2.05, "руб", "вес - ", 4120, "гр"],
                      "маффин": ["состав - мука, дрожжи, сахар, фруктовый джем",
                                 "цена за 100 гр -", 1.80, "руб", "вес - ", 6100, "гр"],
                      "желе": ["состав - желатин, фруктовый сироп",
                               "цена за 100 гр -", 1.10, "руб", "вес - ", 1290, "гр"],
                      "пастила": ["состав - яичный белок, сахар, загуститель",
                                  "цена за 100 гр -", 1.20, "руб", "вес -", 2120, "гр"],
                      "пахлава": ["состав - мука, грецкий орех, арахис, мёд",
                                  "цена за 100 гр -", 1.50, "руб", " вес -", 2140, "гр"]}

customer = int(input("""Наберите 1, 2, 3 или 4, если Вы хотите посмотреть описание, цену, 
                     количество или всю информацию о продукции.
                     Наберите 5, если Вы хотите что-то приобрести :"""))

try:
    if customer == 1:
        for key, value in confectionery_dict.items():
            print(key, ":", value[0])

    elif customer == 2:
        for key, value in confectionery_dict.items():
            print(key, ":", value[1:4])

    elif customer == 3:
        for key, value in confectionery_dict.items():
            print(key, ":", value[4:])

    elif customer == 4:
        for key, value in confectionery_dict.items():
            print(key, ":", value)

    elif customer == 5:
        cost_of_production = 0

        for key, value in confectionery_dict.items():
            i = 1
            while i != 0:
                purchase = input("Введите название продукции :").lower()
                number_of_products = int(input("Введите количество продукции в граммах или 0 для завершения :"))
                cost_of_production += float(confectionery_dict[purchase][2]) * (number_of_products / 100)
                remainder_of_production = int(confectionery_dict[purchase][5]) - number_of_products
                print(f"{purchase}: Oсталось продукции в продаже : {remainder_of_production} грамм")
                i = int(input("Enter 1 to continue, or 0 to complete :"))

            if i == 0:
                print(f"Стоимость приобретенной продукции равна: {cost_of_production} руб")
                break

except KeyError:
    print("Нет такой продукции")

finally:
    print("До свидания!")
