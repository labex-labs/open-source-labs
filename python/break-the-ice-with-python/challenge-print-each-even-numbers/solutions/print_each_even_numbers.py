def print_each_even_numbers():
    lst = []

    for i in range(1000, 2201):
        flag = 1
        for j in str(i):          # every integer number i is converted into string
            if ord(j) % 2 != 0:     # ord returns ASCII value and j is every digit of i
                flag = 0          # flag becomes zero if any odd digit found
        if flag == 1:
            lst.append(str(i))    # i is stored in list as string

    print(",".join(lst))


print_each_even_numbers()
