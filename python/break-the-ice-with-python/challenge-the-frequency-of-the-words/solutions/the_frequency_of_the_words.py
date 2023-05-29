def the_frequency_of_the_words():
    ss = input().split()
    word = sorted(set(ss))     # split words are stored and sorted as a set

    for i in word:
        print("{0}:{1}".format(i, ss.count(i)))


the_frequency_of_the_words()
