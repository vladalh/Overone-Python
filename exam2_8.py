with open("file_name.txt", "r", encoding="utf-8") as file:
    sum_of_points = 0
    numder_stud = 0

    for line in file:
        line_length = int(line[len(line) - 2])
        sum_of_points += line_length

        if line_length < 3:
            print(line[0: -2])
        numder_stud += 1

    print("Average score: {0:.3f}".format(sum_of_points / numder_stud))
