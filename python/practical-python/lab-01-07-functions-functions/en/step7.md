# Exercise 1.30: Turning a script into a function

Take the code you wrote for the `pcost.py` program in Exercise 1.27 and turn it into a function `portfolio_cost(filename)`. This function takes a filename as input, reads the portfolio data in that file, and returns the total cost of the portfolio as a float.

To use your function, change your program so that it looks something like this:

```python
# pcost.py
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
```

When you run your program, you should see the same output as before. After you've run your program, you can also call your function interactively by typing this:

```bash
$ python3 -i pcost.py
```

This will allow you to call your function from the interactive mode.

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

Being able to experiment with your code interactively is useful for testing and debugging.
