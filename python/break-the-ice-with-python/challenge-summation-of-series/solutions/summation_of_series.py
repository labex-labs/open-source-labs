def summation_of_series():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i / (i + 1)
    print(round(sum, 2))

    return round(sum, 2)


summation_of_series()
