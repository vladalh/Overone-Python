import csv
import json




fileus = ""
fileeurope = ""
filejapan = ""

formatfile = input("Enter the file format for saving data: txt, csv or json: ")

cars = {}
car_us = {}
car_europe = {}
car_japan = {}

car_us_list = []
car_europe_list = []
car_japan_list = []

with open(f"cars.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    header = next(csv_reader)

    for line in csv_reader:
        if "US" in line:
            car_us_list.append(line)
        elif "Europe" in line:
            car_europe_list.append(line)
        elif "Japan" in line:
            car_japan_list.append(line)



with open(f"fileus.{formatfile}", "w", encoding="utf-8") as cars_file:
    if formatfile == "txt":
        for car in car_us_list:
            car = " ".join(car) + "\n"
            cars_file.write(car_us_list)

    elif formatfile == "csv":
        columns = ["Car", "MPG", "Cylinders", "Displacement", "Horsepower",
                   "Weight", "Acceleration", "Model", "Origin"]
        csv_file = csv.DictWriter(cars_file, fieldnames=columns)
        csv_file.writeheader()
        csv_file.writerows(car_us_list)

    elif formatfile == "json":
        json_file = json.dump(car_us_list, cars_file, indent=4)

for car in car_europe_list:
    print(car)

for car in car_japan_list:
    print(car)
