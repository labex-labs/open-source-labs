import random


def generate_special_random_numbers():
    resp = [i for i in range(10, 151) if i % 35 == 0]
    print(random.choice(resp))


generate_special_random_numbers()
