def find_runner_up_scores():
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr = sorted(arr)
    print(arr[-2])

find_runner_up_scores()