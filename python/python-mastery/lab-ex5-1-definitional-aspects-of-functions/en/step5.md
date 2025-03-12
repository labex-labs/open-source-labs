# Adding Type Hints

In Python 3.5 and later versions, type hints are supported. Type hints are a way to indicate the expected data types of variables, function parameters, and return values in your code. They don't change how the code runs, but they make the code more readable and can help catch certain types of errors before the code is actually run. Now, let's add type hints to our CSV reader functions.

1. Open the `reader.py` file and update it to include type hints:

```python
# reader.py

import csv
from typing import List, Callable, Dict, Any, Type, Optional, TextIO, Iterator, TypeVar

# Define a generic type for the class parameter
T = TypeVar('T')

def csv_as_dicts(lines: Iterator[str],
                types: List[Callable[[str], Any]],
                headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records: List[Dict[str, Any]] = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterator[str],
                    cls: Type[T],
                    headers: Optional[List[str]] = None) -> List[T]:
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records: List[T] = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str,
                     types: List[Callable[[str], Any]],
                     headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename: str,
                         cls: Type[T],
                         headers: Optional[List[str]] = None) -> List[T]:
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

Let's understand the key changes we've made in the code:

1. We imported types from the `typing` module. This module provides a set of types that we can use to define type hints. For example, `List`, `Dict`, and `Optional` are types from this module.
2. We added a generic type variable `T` to represent the class type. A generic type variable allows us to write functions that can work with different types in a type-safe way.
3. We added type hints to all function parameters and return values. This makes it clear what types of arguments a function expects and what type of value it returns.
4. We used appropriate container types like `List`, `Dict`, and `Optional`. `List` represents a list, `Dict` represents a dictionary, and `Optional` indicates that a parameter can either have a certain type or be `None`.
5. We used `Callable` for the type conversion functions. `Callable` is used to indicate that a parameter is a function that can be called.
6. We used the generic `T` to express that `csv_as_instances` returns a list of instances of the class passed in. This helps the IDE and other tools understand the type of the returned objects.

7. Now, let's create a simple test file to ensure everything still works properly:

```python
# test_types.py

import reader
import stock

# The functions should work exactly as before
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First item:", portfolio[0])

# But now we have better type checking and IDE support
stock_portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst stock:", stock_portfolio[0])

# We can see that stock_portfolio is a list of Stock objects
# This helps IDEs provide better code completion
first_stock = stock_portfolio[0]
print(f"\nName: {first_stock.name}")
print(f"Shares: {first_stock.shares}")
print(f"Price: {first_stock.price}")
print(f"Value: {first_stock.shares * first_stock.price}")
```

3. Run the test script from the terminal:

```bash
python test_types.py
```

The output should look similar to:

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

Type hints don't change how the code runs, but they provide several benefits:

1. They offer better IDE support with code completion. When you use an IDE like PyCharm or VS Code, it can use the type hints to suggest the correct methods and attributes for your variables.
2. They provide clearer documentation about expected parameter and return types. Just by looking at the function definition, you can tell what types of arguments it expects and what type of value it returns.
3. They allow you to use static type checkers like mypy to catch errors early. Static type checkers analyze your code without running it and can find type-related errors before you run the code.
4. They improve code readability and maintainability. When you or other developers come back to the code later, it's easier to understand what the code is doing.

In a large codebase, these benefits can significantly reduce bugs and make the code easier to understand and maintain.

**Note:** Type hints are optional in Python, but they're increasingly used in professional code. Libraries like those in the Python standard library and many popular third-party packages now include extensive type hints.
