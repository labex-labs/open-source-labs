# Defining Functions

It is a good idea to put all of the code related to a single _task_ all in one place. Use a function.

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

A function also simplifies repeated operations.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```
