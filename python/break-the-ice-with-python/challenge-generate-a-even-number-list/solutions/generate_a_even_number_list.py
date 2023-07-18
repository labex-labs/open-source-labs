import random


def generate_a_even_number_list():
    resp = random.sample(range(100, 201, 2), 5)
    print(resp)


generate_a_even_number_list()
