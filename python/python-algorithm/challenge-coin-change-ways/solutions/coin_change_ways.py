def change_ways(n, coins):
    arr = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
    return 0 if n == 0 else arr[n]
