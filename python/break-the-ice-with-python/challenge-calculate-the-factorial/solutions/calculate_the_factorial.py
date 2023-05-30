def calculate_the_factorial():
    n = int(input())    # input() function takes input as string type
    # int() converts it to integer type
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)


calculate_the_factorial()
