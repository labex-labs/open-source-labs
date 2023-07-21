import random


def generate_a_number_list():
    resp = random.sample(range(100, 201), 5)
    print(resp)


generate_a_number_list()
