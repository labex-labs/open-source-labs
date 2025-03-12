# Understanding First-Class Objects in Python

In Python, everything is treated as an object. This includes functions and types. What does this mean? Well, it means that you can store functions and types in data structures, pass them as arguments to other functions, and even return them from other functions. This is a very powerful concept, and we're going to explore it using CSV data processing as an example.

## Exploring First-Class Types

First, let's start the Python interpreter. Open a new terminal in the WebIDE and type the following command. This command will start the Python interpreter, which is where we'll be running our Python code.

```bash
python3
```

When working with CSV files in Python, we often need to convert the strings we read from these files into appropriate data types. For example, a number in a CSV file might be read as a string, but we want to use it as an integer or a float in our Python code. To do this, we can create a list of conversion functions.

```python
coltypes = [str, int, float]
```

Notice that we're creating a list that contains the actual type functions, not strings. In Python, types are first-class objects, which means we can treat them just like any other object. We can put them in lists, pass them around, and use them in our code.

Now, let's read some data from a portfolio CSV file to see how we can use these conversion functions.

```python
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
```

When you run this code, you should see output similar to the following. This is the first row of data from the CSV file, represented as a list of strings.

```
['AA', '100', '32.20']
```

Next, we'll use the `zip` function. The `zip` function takes multiple iterables (like lists or tuples) and pairs up their elements. We'll use it to pair each value from the row with its corresponding type conversion function.

```python
r = list(zip(coltypes, row))
print(r)
```

This will produce the following output. Each pair contains a type function and a string value from the CSV file.

```
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

Now that we have these pairs, we can apply each function to convert the values to their appropriate types.

```python
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
```

The output will show that the values have been converted to their appropriate types. The string 'AA' remains a string, '100' becomes the integer 100, and '32.20' becomes the float 32.2.

```
['AA', 100, 32.2]
```

We can also combine these values with their column names to create a dictionary. A dictionary is a useful data structure in Python that allows us to store key - value pairs.

```python
record_dict = dict(zip(headers, record))
print(record_dict)
```

The output will be a dictionary where the keys are the column names and the values are the converted data.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

You can perform all these steps in a single comprehension. A comprehension is a concise way to create lists, dictionaries, or sets in Python.

```python
result = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(result)
```

The output will be the same dictionary as before.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

When you're done working in the Python interpreter, you can exit it by typing the following command.

```python
exit()
```

This demonstration shows how Python's treatment of functions as first-class objects enables powerful data processing techniques. By being able to treat types and functions as objects, we can write more flexible and concise code.
