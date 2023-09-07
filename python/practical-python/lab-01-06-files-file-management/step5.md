# Exercise 1.27: Reading a data file

Now that you know how to read a file, let's write a program to perform a simple calculation.

The columns in `portfolio.csv` correspond to the stock name, number of shares, and purchase price of a single stock holding. Write a program called `pcost.py` in `/home/labex/project` directory that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

_Hint: to convert a string to an integer, use `int(s)`. To convert a string to a floating point, use `float(s)`._

Your program should print output such as the following:

```bash
Total cost 44671.15
```

Here's a solution:
```python
# pcost.py

total_cost = 0.0

with open("portfolio.csv", "rt") as f:
    headers = next(f)
    for line in f:
        row = line.split(",")
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price

print("Total cost", total_cost)
```
