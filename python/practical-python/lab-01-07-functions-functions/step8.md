# Exercise 1.31: Error handling

What happens if you try your function on a file with some missing fields?

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

At this point, you're faced with a decision. To make the program work you can either sanitize the original input file by eliminating bad lines or you can modify your code to handle the bad lines in some manner.

Modify the `pcost.py` program to catch the exception, print a warning message, and continue processing the rest of the file.

Here's a solution:

```python
# pcost.py

import sys


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        lines = f.readlines()
        headers = lines[0].strip().split(",")
        for line in lines[1:]:
            fields = line.strip().split(",")
            if len(fields) < 3:
                print("Skipping invalid row:", line)
                continue
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Skipping invalid row:", line)

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
```