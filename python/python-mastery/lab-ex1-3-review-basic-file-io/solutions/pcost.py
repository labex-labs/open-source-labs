# pcost.py

total_cost = 0.0

filePath = "/home/labex/project/portfolio.dat"

with open(filePath, "r") as f:
    for line in f:
        fields = line.split()
        nshares = int(fields[1])
        price = float(fields[2])
        total_cost = total_cost + nshares * price

print(total_cost)
