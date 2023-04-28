def factorial(num):
    if not ((num >= 0) and (num % 1 == 0)):
        raise Exception("Number can't be floating point or negative.")
    return 1 if num == 0 else num * factorial(num - 1)
