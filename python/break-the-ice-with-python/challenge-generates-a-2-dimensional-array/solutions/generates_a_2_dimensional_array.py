def generates_a_2_dimensional_array():
    x, y = map(int, input().split(","))
    lst = [[i * j for j in range(y)] for i in range(x)]
    print(lst)


generates_a_2_dimensional_array()
