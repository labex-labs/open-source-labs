from math import sqrt


def calculate_the_value_of_formula():
    C, H = 50, 30

    def calc(D):
        return sqrt((2*C*D)/H)

    # splits in comma position and set up in list
    D = input().split(',')
    # using comprehension method. It works in order of the previous code
    D = [str(round(calc(int(i)))) for i in D]
    print(",".join(D))


calculate_the_value_of_formula()
