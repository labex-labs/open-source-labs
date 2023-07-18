def print_words_in_order():
    lst = input().split(',')
    lst.sort()
    print(",".join(lst))


print_words_in_order()
