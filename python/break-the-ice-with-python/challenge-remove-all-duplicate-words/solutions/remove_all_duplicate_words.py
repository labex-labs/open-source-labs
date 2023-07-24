def remove_all_duplicate_words():
    word = input().split()

    for i in word:
        # count function returns total repeatation of an element that is send as argument
        if word.count(i) > 1:
            word.remove(i)     # removes exactly one element per call

    word.sort()
    print(" ".join(word))


remove_all_duplicate_words()
