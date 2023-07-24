def print_lists_symmetric_difference():
    n = int(input())
    set1 = set(map(int, input().split()))

    m = int(input())
    set2 = set(map(int, input().split()))

    ans = list(set1 ^ set2)
    ans = sorted(ans)
    for i in ans:
        print(i)


print_lists_symmetric_difference()
