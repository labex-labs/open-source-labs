# Using enumerate() and zip() Functions

In this step, you will learn about two useful built-in functions for iteration: `enumerate()` and `zip()`.

## Counting with enumerate()

The `enumerate()` function is very useful when you need to keep track of the index or position while iterating. It returns pairs of (index, value) for each item in the sequence.

Continue using the Python interpreter from the previous step, or start a new session if needed:

```python
# If you're starting a new session, reload the data first:
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Use enumerate to get row numbers
for rowno, row in enumerate(rows):
    print(rowno, row)
```

Output:

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

You can combine `enumerate()` with unpacking for more readable code:

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

Output:

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

Notice how we used an extra pair of parentheses around `(name, shares, price)` to properly unpack the row data.

## Pairing Data with zip()

The `zip()` function is used to combine corresponding elements from multiple sequences. It creates an iterator that produces tuples containing elements from each sequence.

Let's see how to use `zip()` with our headers and row data:

```python
# Recall the headers variable from earlier
print(headers)  # Should show ['name', 'shares', 'price']

# Get the first row
row = rows[0]
print(row)      # Should show ['AA', '100', '32.20']

# Use zip to pair column names with values
for col, val in zip(headers, row):
    print(col, val)
```

Output:

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

One common use of `zip()` is to create dictionaries from key-value pairs:

```python
# Create a dictionary from headers and row values
record = dict(zip(headers, row))
print(record)
```

Output:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

We can extend this to convert all rows to dictionaries:

```python
# Convert all rows to dictionaries
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

Output:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```

This technique of using `zip()` to create dictionaries is very common in data processing applications, especially when working with CSV files where the first row contains headers.
