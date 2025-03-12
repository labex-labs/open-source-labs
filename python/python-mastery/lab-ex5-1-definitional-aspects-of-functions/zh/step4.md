# 处理没有表头的 CSV 文件

在数据处理领域，并非所有 CSV 文件的第一行都包含表头。表头是 CSV 文件中为每列赋予的名称，它能帮助我们了解每列所包含的数据类型。当 CSV 文件没有表头时，我们需要一种方法来妥善处理它。在本节中，我们将修改函数，允许调用者手动提供表头，这样我们就可以处理有表头和没有表头的 CSV 文件。

1. 打开 `reader.py` 文件，并更新它以包含表头处理功能：

```python
# reader.py

import csv

def csv_as_dicts(lines, types, headers=None):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, headers=None):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, headers=None):
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

def read_csv_as_instances(filename, cls, headers=None):
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

让我们来理解这些函数所做的关键更改：

1. 我们为所有函数添加了一个 `headers` 参数，并将其默认值设置为 `None`。这意味着如果调用者没有提供任何表头，函数将使用默认行为。
2. 在 `csv_as_dicts` 函数中，只有当 `headers` 参数为 `None` 时，我们才将第一行用作表头。这使我们能够自动处理有表头的文件。
3. 在 `csv_as_instances` 函数中，只有当 `headers` 参数为 `None` 时，我们才跳过第一行。这是因为如果我们提供了自己的表头，文件的第一行就是实际数据，而不是表头。

4. 让我们使用没有表头的文件来测试这些修改。创建一个名为 `test_headers.py` 的文件：

```python
# test_headers.py

import reader
import stock

# Define column names for the file without headers
column_names = ['name', 'shares', 'price']

# Test reading a file without headers
portfolio = reader.read_csv_as_dicts('portfolio_noheader.csv',
                                     [str, int, float],
                                     headers=column_names)
print("First item from file without headers:", portfolio[0])
print("Total items:", len(portfolio))

# Test reading the same file as instances
portfolio = reader.read_csv_as_instances('portfolio_noheader.csv',
                                        stock.Stock,
                                        headers=column_names)
print("\nFirst item as Stock instance:", portfolio[0])
print("Total items:", len(portfolio))

# Verify that original functionality still works
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item from file with headers:", portfolio[0])
```

在这个测试脚本中，我们首先为没有表头的文件定义列名。然后，我们测试将没有表头的文件读取为字典列表和类实例列表。最后，我们通过读取有表头的文件来验证原始功能仍然有效。

3. 从终端运行测试脚本：

```bash
python test_headers.py
```

输出应该类似于：

```
First item from file without headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7

First item from file with headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

这个输出证实了我们的函数现在可以处理有表头和没有表头的 CSV 文件。用户可以在需要时提供列名，或者依靠从第一行读取表头的默认行为。

通过进行此修改，我们的 CSV 读取函数现在更加通用，可以处理更广泛的文件格式。这是使我们的代码在不同场景中更加健壮和有用的重要一步。
