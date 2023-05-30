def solve(numheads, numlegs):
    ns = "No solutions!"
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns, ns


numheads = 35
numlegs = 94
solutions = solve(numheads, numlegs)
print(solutions)
