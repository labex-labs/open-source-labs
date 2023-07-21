# Dict Construction

Example of building a dict from scratch.

```python
prices = {} # Initial empty dict

# Insert new items
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

An example populating the dict from the contents of a file.

```python
prices = {} # Initial empty dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

Note: If you try this on the `Data/prices.csv` file, you'll find that
it almost works--there's a blank line at the end that causes it to
crash. You'll need to figure out some way to modify the code to
account for that (see Exercise 2.6).
