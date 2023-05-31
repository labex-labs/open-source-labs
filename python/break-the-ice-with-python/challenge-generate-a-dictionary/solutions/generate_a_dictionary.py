def generate_a_dictionary():
    n = int(input())
    ans = {i: i*i for i in range(1, n+1)}
    print(ans)


generate_a_dictionary()
