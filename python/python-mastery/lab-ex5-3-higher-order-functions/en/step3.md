# Refactoring Existing Functions

Now, we have created a higher-order function named `convert_csv()`. Higher-order functions are functions that can take other functions as arguments or return functions as results. They are a powerful concept in Python that can help us write more modular and reusable code. In this section, we will use this higher-order function to refactor the original functions `csv_as_dicts()` and `csv_as_instances()`. Refactoring is the process of restructuring existing code without changing its external behavior, aiming to improve its internal structure, such as eliminating code duplication.

Let's start by opening the `reader.py` file in the WebIDE. We will update the functions as follows:

1. First, we'll replace the `csv_as_dicts()` function. This function is used to convert lines of CSV data into a list of dictionaries. Here's the new code:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

In this code, we define an inner function `dict_converter` that takes `headers` and `row` as arguments. It uses a dictionary comprehension to create a dictionary where the keys are the header names, and the values are the result of applying the corresponding type conversion function to the values in the row. Then, we call the `convert_csv()` function with the `dict_converter` function as an argument.

2. Next, we'll replace the `csv_as_instances()` function. This function is used to convert lines of CSV data into a list of instances of a given class. Here's the new code:

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

In this code, we define an inner function `instance_converter` that takes `headers` and `row` as arguments. It calls the `from_row` class method of the given class `cls` to create an instance from the row. Then, we call the `convert_csv()` function with the `instance_converter` function as an argument.

After refactoring these functions, we need to test them to make sure they still work as expected. To do this, we'll run the following commands in a Python shell:

```bash
cd ~/project
python3 -i reader.py
```

The `cd ~/project` command changes the current working directory to the `project` directory. The `python3 -i reader.py` command runs the `reader.py` file in interactive mode, which means we can continue to execute Python code after the file has finished running.

Once the Python shell is open, we'll run the following code to test the refactored functions:

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

In this code, we first define a simple `Stock` class for testing. The `__init__` method initializes the attributes of a `Stock` instance. The `from_row` class method creates a `Stock` instance from a row of CSV data. The `__repr__` method provides a string representation of the `Stock` instance.

Then, we test the `csv_as_dicts()` function by opening the `portfolio.csv` file and passing it to the function along with a list of type conversion functions. We print the first dictionary in the resulting list.

Finally, we test the `csv_as_instances()` function by opening the `portfolio.csv` file and passing it to the function along with the `Stock` class. We print the first instance in the resulting list.

If everything is working correctly, you should see output similar to the following:

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

This output indicates that our refactored functions are working correctly. We've successfully eliminated the code duplication while maintaining the same functionality.

To exit the Python shell, you can type `exit()` or press Ctrl+D.
