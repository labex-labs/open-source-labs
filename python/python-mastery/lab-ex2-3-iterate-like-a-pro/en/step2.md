# Using enumerate() and zip() Functions

In this step, we're going to explore two incredibly useful built - in functions in Python that are essential for iteration: `enumerate()` and `zip()`. These functions can significantly simplify your code when you're working with sequences.

## Counting with enumerate()

When you're iterating over a sequence, you might often need to keep track of the index or position of each item. That's where the `enumerate()` function comes in handy. The `enumerate()` function takes a sequence as input and returns pairs of (index, value) for each item in that sequence.

If you've been following along in the Python interpreter from the previous step, you can continue using it. If not, start a new session. Here's how you can set up the data if you're starting fresh:

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

When you run the above code, the `enumerate(rows)` function will generate pairs of an index (starting from 0) and the corresponding row from the `rows` sequence. The `for` loop then unpacks these pairs into the variables `rowno` and `row`, and we print them out.

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

We can make the code even more readable by combining `enumerate()` with unpacking. Unpacking allows us to directly assign the elements of a sequence to individual variables.

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

In this code, we're using an extra pair of parentheses around `(name, shares, price)` to properly unpack the row data. The `enumerate(rows)` still gives us the index and the row, but now we're unpacking the row into `name`, `shares`, and `price` variables.

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

## Pairing Data with zip()

The `zip()` function is another powerful tool in Python. It's used to combine corresponding elements from multiple sequences. When you pass multiple sequences to `zip()`, it creates an iterator that produces tuples, where each tuple contains elements from each of the input sequences at the same position.

Let's see how we can use `zip()` with the `headers` and `row` data we've been working with.

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

In this code, `zip(headers, row)` takes the `headers` sequence and the `row` sequence and pairs up their corresponding elements. The `for` loop then unpacks these pairs into `col` (for the column name from `headers`) and `val` (for the value from `row`), and we print them out.

Output:

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

One very common use of `zip()` is to create dictionaries from key - value pairs. In Python, a dictionary is a collection of key - value pairs.

```python
# Create a dictionary from headers and row values
record = dict(zip(headers, row))
print(record)
```

Here, `zip(headers, row)` creates pairs of column names and values, and the `dict()` function takes these pairs and turns them into a dictionary.

Output:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

We can extend this idea to convert all rows in our `rows` sequence to dictionaries.

```python
# Convert all rows to dictionaries
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

In this loop, for each row in `rows`, we use `zip(headers, row)` to create key - value pairs and then `dict()` to turn those pairs into a dictionary. This technique is very common in data processing applications, especially when working with CSV files where the first row contains headers.

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
