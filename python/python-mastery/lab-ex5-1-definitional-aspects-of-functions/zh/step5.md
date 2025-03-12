# 添加类型提示

在 Python 3.5 及更高版本中，支持类型提示。类型提示是一种在代码中指明变量、函数参数和返回值预期数据类型的方式。它们不会改变代码的运行方式，但能让代码更易读，还能在代码实际运行前帮助捕获某些类型的错误。现在，让我们为 CSV 读取函数添加类型提示。

1. 打开 `reader.py` 文件，并更新它以包含类型提示：

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

让我们来理解代码中所做的关键更改：

1. 我们从 `typing` 模块导入了类型。这个模块提供了一组可用于定义类型提示的类型。例如，`List`、`Dict` 和 `Optional` 就是这个模块中的类型。
2. 我们添加了一个泛型类型变量 `T` 来表示类的类型。泛型类型变量允许我们编写能以类型安全的方式处理不同类型的函数。
3. 我们为所有函数参数和返回值添加了类型提示。这使得函数期望的参数类型以及返回值的类型一目了然。
4. 我们使用了合适的容器类型，如 `List`、`Dict` 和 `Optional`。`List` 表示列表，`Dict` 表示字典，`Optional` 表示参数可以是某种类型，也可以是 `None`。
5. 我们对类型转换函数使用了 `Callable`。`Callable` 用于表明参数是一个可调用的函数。
6. 我们使用泛型 `T` 来表示 `csv_as_instances` 返回传入类的实例列表。这有助于 IDE 和其他工具理解返回对象的类型。

7. 现在，让我们创建一个简单的测试文件，以确保一切仍然正常工作：

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

3. 从终端运行测试脚本：

```bash
python test_types.py
```

输出应该类似于：

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

类型提示不会改变代码的运行方式，但它们有以下几个好处：

1. 它们能为 IDE 提供更好的代码补全支持。当你使用像 PyCharm 或 VS Code 这样的 IDE 时，它可以利用类型提示为你的变量推荐正确的方法和属性。
2. 它们能更清晰地记录预期的参数和返回类型。只需查看函数定义，你就能知道它期望的参数类型和返回值类型。
3. 它们允许你使用像 mypy 这样的静态类型检查器来提前捕获错误。静态类型检查器在不运行代码的情况下分析代码，并能在你运行代码之前发现与类型相关的错误。
4. 它们能提高代码的可读性和可维护性。当你或其他开发者之后再查看代码时，更容易理解代码的功能。

在大型代码库中，这些好处可以显著减少 bug，并使代码更易于理解和维护。

**注意：** 类型提示在 Python 中是可选的，但在专业代码中越来越常用。Python 标准库中的库以及许多流行的第三方包现在都包含大量的类型提示。
