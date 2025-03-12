# Understanding First-Class Objects in Python

Python treats everything as an object, including functions and types. This makes it possible to store them in data structures, pass them as arguments, and return them from other functions. Let's explore this concept using CSV data processing as an example.

## Exploring First-Class Types

Open a new terminal in the WebIDE and start the Python interpreter by typing:

```bash
python3
```

In Python, we often need to convert strings from CSV files into appropriate data types. We can create a list of conversion functions:

```python
coltypes = [str, int, float]
```

Note how we're creating a list containing the actual type functions, not strings. This is possible because in Python, types are first-class objects.

Let's read some data from a portfolio CSV file to see how we can use these functions:

```python
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
```

You should see output similar to:

```
['AA', '100', '32.20']
```

Now, let's use the `zip` function to pair each value with its corresponding type conversion function:

```python
r = list(zip(coltypes, row))
print(r)
```

This produces:

```
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

Each pair contains a type function and a string value. Now we can apply each function to convert the values:

```python
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
```

Output:

```
['AA', 100, 32.2]
```

Notice how the values have been converted to their appropriate types - the string 'AA' remains a string, '100' becomes the integer 100, and '32.20' becomes the float 32.2.

We can also combine these values with their column names to create a dictionary:

```python
record_dict = dict(zip(headers, record))
print(record_dict)
```

Output:

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

You can perform all these steps in a single comprehension:

```python
result = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(result)
```

Output:

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Exit the Python interpreter by typing:

```python
exit()
```

This demonstration shows how Python's treatment of functions as first-class objects enables powerful data processing techniques.
