def square_each_odd_number():
    seq = input().split(',')
    lst = [int(i) for i in seq]

    def flt(i):  # Define a filter function
        return i % 2 != 0

    result_l = [str(i * i) for i in filter(flt, lst)]
    print(",".join(result_l))


square_each_odd_number()
