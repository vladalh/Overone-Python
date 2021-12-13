import random

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
    for i in range(genre_count + 1):
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
        "genre": genres_set,
        "country": tuple(random.sample(country_of_origin, country_count))}
    a += 1

    cinema_full_dict[movie_number] = cinema_dict

dict_save_path = input("Enter the path to save the movie dictionary: ")

if dict_save_path != "":
    file = open(f"{dict_save_path}/movies.txt", "w", encoding="utf-8")
    for key, value in cinema_full_dict.items():
        file.write(f"{key}: {value}\n")
    file.close()

else:
    file = open("movies.txt", "w", encoding="utf-8")
    for key, value in cinema_full_dict.items():
        file.write(f"{key}: {value}\n")
    file.close()

criterion_list = []

person = input("Enter year, rating, country or genre:")

result_path = input("Enter the path to save the list by selection criterion: ")

if dict_save_path != "":
    try:
        file = open(f"{dict_save_path}/movies.txt", "r", encoding="utf-8")
        for line in file:
            file_list = line.split(",")
            cinema_list.append(file_list)
        file.close()
    except IOError:
        print("No file")

else:
    try:
        file = open("movies.txt", "r", encoding="utf-8")
        for line in file:
            file_list = line.split(",")
            cinema_list.append(file_list)
        file.close()
    except IOError:
        print("No file")

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

        elif person in list(cinema[5]):
            criterion_list.append(cinema)

    else:
        print("The input format does not meet the requirement. Restart the program and re-enter")

result_mmovies = ""

for res in criterion_list:
    result = ",".join(res)
    result_mmovies += result

if result_path != "":
    file = open(f"{result_path}/result_mmovies.txt", "w", encoding="utf-8")
    file.write(result_mmovies)
    file.close()

else:
    file = open("result_mmovies.txt", "w", encoding="utf-8")
    file.write(result_mmovies)
    file.close()

# vladalh@mail.ru
