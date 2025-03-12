# Basic Iteration and Sequence Unpacking

In this step, we'll explore basic iteration using `for` loops and sequence unpacking in Python. Iteration is a fundamental concept in programming, allowing you to go through each item in a sequence one by one. Sequence unpacking, on the other hand, lets you assign individual elements of a sequence to variables in a convenient way.

## Loading Data from a CSV File

Let's start by loading some data from a CSV file. CSV (Comma-Separated Values) is a common file format used to store tabular data. To begin, we need to open a terminal in the WebIDE and start the Python interpreter. This will allow us to run Python code interactively.

```bash
cd ~/project
python3
```

Now that we're in the Python interpreter, we can execute the following Python code to read data from the `portfolio.csv` file. First, we import the `csv` module, which provides functionality for working with CSV files. Then, we open the file and create a `csv.reader` object to read the data. We use the `next` function to get the column headers, and convert the remaining data to a list. Finally, we use the `pprint` function from the `pprint` module to print the rows in a more readable format.

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

The `for` statement in Python is used to iterate over any sequence of data, such as a list, tuple, or string. In our case, we'll use it to iterate over the rows of data we loaded from the CSV file.

```python
for row in rows:
    print(row)
```

This code will go through each row in the `rows` list and print it. You'll see each row of data from our CSV file printed one by one.

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

Python allows you to unpack sequences directly in a `for` loop. This is very useful when you know the structure of each item in the sequence. In our case, each row in the `rows` list contains three elements: a name, the number of shares, and the price. We can unpack these elements directly in the `for` loop.

```python
for name, shares, price in rows:
    print(name, shares, price)
```

This code will unpack each row into the variables `name`, `shares`, and `price`, and then print them. You'll see the data printed in a more readable format.

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

If you don't need some values, you can use `_` as a placeholder to indicate that you don't care about those values. For example, if you only want to print the name and the price, you can use the following code:

```python
for name, _, price in rows:
    print(name, price)
```

This code will ignore the second element in each row and print only the name and the price.

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

For more advanced unpacking, you can use the `*` operator as a wildcard. This allows you to collect multiple elements into a list. Let's group our data by name using this technique.

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

In this code, we first import the `defaultdict` class from the `collections` module. A `defaultdict` is a dictionary that automatically creates a new value (in this case, an empty list) if the key doesn't exist. Then, we use the `*` operator to collect all elements except the first one into a list called `data`. We store this list in the `byname` dictionary, grouped by the name. Finally, we print the data for IBM and iterate through it to print the shares and price.

Output:

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 70.44
```

In this example, `*data` collects all items except the first one into a list, which we then store in a dictionary grouped by name. This is a powerful technique for handling data with variable-length sequences.
