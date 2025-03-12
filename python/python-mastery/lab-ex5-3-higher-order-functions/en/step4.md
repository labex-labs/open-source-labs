# Using the map() Function

In Python, a higher-order function is a function that can take another function as an argument or return a function as a result. Python's `map()` function is a great example of a higher-order function. It's a powerful tool that allows you to apply a given function to each item in an iterable, such as a list or a tuple. After applying the function to each item, it returns an iterator of the results. This feature makes `map()` perfect for processing sequences of data, like rows in a CSV file.

The basic syntax of the `map()` function is as follows:

```python
map(function, iterable, ...)
```

Here, the `function` is the operation you want to perform on each item in the `iterable`. The `iterable` is a sequence of items, like a list or a tuple.

Let's look at a simple example. Suppose you have a list of numbers, and you want to square each number in that list. You can use the `map()` function to achieve this. Here's how you can do it:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

In this example, we first define a list called `numbers`. Then, we use the `map()` function. The `lambda` function `lambda x: x * x` is the operation we want to perform on each item in the `numbers` list. The `map()` function applies this `lambda` function to each number in the list. Since `map()` returns an iterator, we convert it to a list using the `list()` function. Finally, we print the `squared` list, which contains the squared values of the original numbers.

Now, let's take a look at how we can use the `map()` function to modify our `convert_csv()` function. Previously, we used a `for` loop to iterate over the rows in the CSV data. Now, we'll replace that `for` loop with the `map()` function.

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

This updated version of the `convert_csv()` function does exactly the same thing as the previous version, but it uses the `map()` function instead of a `for` loop. The `lambda` function inside the `map()` takes each row from the CSV data and applies the `conversion_func` to it, along with the headers.

Let's test this updated function to make sure it works correctly. First, open your terminal and navigate to the project directory. Then, start the Python interactive shell with the `reader.py` file.

```bash
cd ~/project
python3 -i reader.py
```

Once you're in the Python shell, run the following code to test the updated `convert_csv()` function:

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

After running this code, you should see output similar to the following:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

This output shows that the updated `convert_csv()` function using the `map()` function works correctly, and the functions that rely on it also continue to work as expected.

Using the `map()` function has several advantages:

1. It can be more concise than a `for` loop. Instead of writing multiple lines of code for a `for` loop, you can achieve the same result with a single line using `map()`.
2. It clearly communicates your intent to transform each item in a sequence. When you see `map()`, you immediately know that you're applying a function to each item in an iterable.
3. It can be more memory-efficient because it returns an iterator. An iterator generates values on-the-fly, which means it doesn't store all the results in memory at once. In our example, we converted the iterator returned by `map()` to a list, but in some cases, you can work directly with the iterator to save memory.

To exit the Python shell, you can type `exit()` or press Ctrl+D.
