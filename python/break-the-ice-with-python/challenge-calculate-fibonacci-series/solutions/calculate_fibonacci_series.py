def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)


n = int(input())
print(f(n))
