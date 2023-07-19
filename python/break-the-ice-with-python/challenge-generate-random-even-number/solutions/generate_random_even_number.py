import random


def generate_random_even_number():
    resp = [i for i in range(0, 11, 2)]
    print(random.choice(resp))


generate_random_even_number()
