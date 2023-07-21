def speical_numbers_generator(n):
    if n == 0:
        return
    for i in range(n+1):
        if i % 35 == 0:    # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i


n = int(input())
resp = [str(i) for i in speical_numbers_generator(n)]
print(",".join(resp))
