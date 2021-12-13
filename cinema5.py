import json
import random
import csv


name_cinema_list_1 = ["I", "all", "we", "always", "yesterday", "sailing", "go", "house",
                      "stadium", "clouds", "window", "locked", "a door", "close", "television"]
name_cinema_list_2 = ["airplane", "fly", "run away", "dog", "cat", "arrow", "siren", "moon",
                      "sun", "ship", "a boat", "war", "peace", "bird", "ball"]
name_cinema_list_3 = ["about", "talk", "wedding", "scenario", "dumb", "disabled person", "he",
                      "you", "young woman", "boy", "father", "nanny", "think", "only", "kiss"]

genres_cinema = ["horrors", "fantastic", "thriller", "melodrama", "military", "about love",
                 "comedy", "detective", "erotica", "historical", "cartoon", "western film", "anime"]

country_of_origin = ["USA", "Canada", "France", "Russia", "Italy", "United Kingdom", "Poland",
                     "Germany", "China", "Korea", "Turkey", "Brasil", "Belarus", "Mexico", "Romania"]

a = 1
cinema_full_dict = {}
cinema_dict = {}
cinema_list = []
genres_set = set()
country_set = set()

while a <= 20:
    num = random.randint(1, 1000000)
    cinema_list.append(num)
    if cinema_list.count(num) >= 2:
        num = random.randint(1, 1000000)
        cinema_list.append(num)
    for num in cinema_list:
        movie_number = num
    cinema_list.clear()

    full_name = (str(random.choice(name_cinema_list_1)) + " " + str(random.choice(name_cinema_list_2)) +
                 " " + str(random.choice(name_cinema_list_3)))

    rating = sum([random.randint(1, 100) for k in range(100)]) / 100

    production_year = random.randint(1895, 2021)

    genre_count = random.randint(1, 3)
    for i in range(genre_count):
        genre = random.choice(genres_cinema)
        cinema_list.append(genre)
        genres_set = set(cinema_list)
        if len(genres_set) < genre_count:
            cinema_list.append(random.choice(genres_cinema))
            genres_set = set(cinema_list)
        cinema_list.clear()

    country_count = random.randint(1, 3)
    for j in range(country_count):
        country = random.choice(country_of_origin)
        country_set.add(country)
        if len(country_set) < country_count:
            country_set.add(random.choice(country_of_origin))

    cinema_dict = {
        "movie number": movie_number,
        "movie title": full_name,
        "mark": rating,
        "year of issue": production_year,
        "genre": list(genres_set),
        "country": tuple(random.sample(country_of_origin, country_count))}
    a += 1

    cinema_full_dict[movie_number] = cinema_dict

file_format_list = ["txt", "csv", "json"]

file_format = input("Enter the file format for saving data: txt, csv or json: ")

dict_save_path = input("Enter the path to save the movie dictionary: (optional step, you can click 'enter') ")

if file_format not in file_format_list:
    print("You entered the wrong file format")
    exit(0)

else:
    try:
        with open(f"{dict_save_path}movies.{file_format}", "w", encoding="utf-8") as file:
            if file_format == "txt":
                for key, value in cinema_full_dict.items():
                    txt_file = file.write(f"{key}: {value}\n")

            elif file_format == "csv":
                columns = ["movie number", "movie title", "mark", "year of issue", "genre", "country"]
                csv_file = csv.DictWriter(file, fieldnames=columns)
                csv_file.writeheader()
                csv_file.writerows(cinema_full_dict.values())

            elif file_format == "json":
                json_file = json.dump(cinema_full_dict, file, indent=4)

    except IOError:
        print("Unable to file or read data")

criterion_list = []

person = input("Enter year, rating, country or genre:")

if 0 > int(person) > 100 or 1895 > int(person) > 2021 or person not in genres_cinema or \
        person not in country_of_origin:
    print("Invalid search data")
    exit(0)
else:
    result_path = input("Enter the path to save the list by selection criterion: (optional step, you can click 'enter')")

result_mmovies = ""

try:
    with open(f"{dict_save_path}movies.{file_format}", "r", encoding="utf-8") as file:
        if file_format == "txt":
            for line in file:
                file_list = line.split(",")
                cinema_list.append(file_list)

            for cinema in cinema_list:
                if person.isdigit():
                    if int(person) > 1895:
                        cin1 = cinema[3].strip().split(":")
                        cin2 = cin1[1]
                        if int(person) <= int(cin2):
                            criterion_list.append(cinema)

                    elif int(person) < 100:
                        cin3 = cinema[2].strip().split(":")
                        cin4 = cin3[1]
                        if int(person) <= float(cin4):
                            criterion_list.append(cinema)

                elif person.isalpha():
                    if person in cinema[4]:
                        criterion_list.append(cinema)

                    elif person in cinema[5]:
                        criterion_list.append(cinema)

        elif file_format == "csv":
            csv_reader = csv.DictReader(file, delimiter=",")
            for line in csv_reader:
                if any(line):
                    cinema_list.append(line)

            for cinema in cinema_list:
                if person.isdigit():
                    if int(person) >= 1895 and int(person) <= int(cinema["year of issue"]):
                        criterion_list.append(cinema)

                    elif int(person) <= 100 and int(person) <= float(cinema["mark"]):
                        criterion_list.append(cinema)

                elif person.isalpha():
                    if person in cinema["genre"]:
                        criterion_list.append(cinema)

                    elif person in cinema["country"]:
                        criterion_list.append(cinema)

        elif file_format == 'json':
            json_data = json.load(file)

            for cin in json_data:
                if person.isdigit():
                    if int(person) >= 1895 and int(person) <= json_data[cin]["year of issue"]:
                        criterion_list.append(json_data[cin])

                    elif int(person) <= 100 and int(person) <= float(json_data[cin]["mark"]):
                        criterion_list.append(json_data[cin])

                elif person.isalpha():
                    if person in json_data[cin]["genre"]:
                        criterion_list.append(json_data[cin])

                    elif person in json_data[cin]["country"]:
                        criterion_list.append(json_data[cin])

except FileNotFoundError:
    print("Sorry, the file specified does not exist")

except IOError:
    print("Unable to file or read data")

for res in criterion_list:
    result = ",".join(res)
    result_mmovies += result
try:
    with open(f"{result_path}result_mmovies.{file_format}", "w", encoding="utf-8") as file:
        if file_format == "txt":
            file.write(result_mmovies)

        elif file_format == "csv":
            columns = ["movie number", "movie title", "mark", "year of issue", "genre", "country"]
            csv_file = csv.DictWriter(file, fieldnames=columns)
            csv_file.writeheader()
            csv_file.writerows(criterion_list)

        elif file_format == "json":
            json_file = json.dump(criterion_list, file, indent=4)

except FileNotFoundError:
    print("Sorry, the file specified does not exist")

except IOError:
    print("Unable to file or read data")

else:
    print("The program has completed successfully")

# vladalh@mail.ru
