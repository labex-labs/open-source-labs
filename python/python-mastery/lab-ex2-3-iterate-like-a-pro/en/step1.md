# Basic Iteration and Sequence Unpacking

In this step, you will learn about basic iteration with `for` loops and sequence unpacking in Python.

## Loading Data from a CSV File

Let's start by loading some data from a CSV file. Open a terminal in the WebIDE and start the Python interpreter:

```bash
cd ~/project
python3
```

Now, execute the following Python code to read data from the `portfolio.csv` file:

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Get the column headers
rows = list(f_csv)       # Convert the remaining data to a list
from pprint import pprint
pprint(rows)             # Pretty print the rows
```

You should see output similar to this:

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## Basic Iteration with `for` Loops

The `for` statement in Python iterates over any sequence of data. Let's see how to use it with our CSV data:

```python
for row in rows:
    print(row)
```

This will print each row of data from our CSV file:

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## Sequence Unpacking in Loops

Python allows you to unpack sequences directly in a `for` loop. This is very useful when you know the structure of each item in the sequence:

```python
for name, shares, price in rows:
    print(name, shares, price)
```

Output:

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

If you don't need some values, you can use `_` as a placeholder to indicate that you don't care about those values:

```python
for name, _, price in rows:
    print(name, price)
```

Output:

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## Extended Unpacking with the `*` Operator

For more advanced unpacking, you can use the `*` operator as a wildcard. Let's group our data by name:

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Print the data for IBM
print(byname['IBM'])

# Iterate through IBM's data
for shares, price in byname['IBM']:
    print(shares, price)
```

Output:

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 70.44
```

In this example, `*data` collects all items except the first one into a list, which we then store in a dictionary grouped by name.
