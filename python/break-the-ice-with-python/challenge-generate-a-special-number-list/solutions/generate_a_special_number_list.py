import random


def generate_a_special_number_list():
    lst = [i for i in range(1, 1001) if i % 35 == 0]
    resp = random.sample(lst, 5)
    print(resp)


generate_a_special_number_list()
