def calculating_letter_frequencies():
    word = input()
    dct = {}
    for i in word:
        dct[i] = dct.get(i, 0) + 1

    dct = sorted(dct.items(), key=lambda x: (-x[1], x[0]))
    for i in dct:
        print(i[0], i[1])


calculating_letter_frequencies()
