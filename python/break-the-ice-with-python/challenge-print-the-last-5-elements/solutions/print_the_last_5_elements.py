def print_the_last_5_elements():
    li = list()
    for i in range(1, 21):
        li.append(i**2)
    print(li[-5:])


print_the_last_5_elements()
