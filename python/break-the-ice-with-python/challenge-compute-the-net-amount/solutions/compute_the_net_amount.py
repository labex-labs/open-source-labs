def compute_the_net_amount():
    total = 0
    while True:
        s = input().split()
        if not s:            # break if the string is empty
            break
        # two inputs are distributed in cm and num in string data type
        cm, num = map(str, s)

        if cm == 'D':
            total += int(num)
        if cm == 'W':
            total -= int(num)

    print(total)


compute_the_net_amount()
