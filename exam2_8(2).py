with open("file_name.txt", "r", encoding="utf-8") as file:
    sum_point = 0
    i = 0

    for line in file:
        line1 = line.strip()
        sum_point += int(line1[-1])
        if int(line1[-1]) < 3:
            print(line1[0: -1])

        i += 1
    print("Average score: {0:.3f}".format(sum_point / i))
