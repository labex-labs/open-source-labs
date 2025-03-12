# 让函数更具灵活性

目前，我们的函数仅限于读取由文件名指定的文件，这限制了它们的可用性。在编程中，让函数更具灵活性通常是有益的，这样它们就能处理不同类型的输入。就我们的情况而言，如果我们的函数能够处理任何能产生行的可迭代对象，比如文件对象或其他数据源，那就太好了。这样，我们就能在更多场景中使用这些函数，例如从压缩文件或其他数据流中读取数据。

让我们重构代码以实现这种灵活性：

1. 打开 `reader.py` 文件。我们将对其进行修改，添加一些新函数。这些新函数将使我们的代码能够处理不同类型的可迭代对象。以下是你需要添加的代码：

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

让我们仔细看看我们是如何重构代码的：

1. 我们创建了两个更通用的函数 `csv_as_dicts()` 和 `csv_as_instances()`。这些函数旨在处理任何能产生 CSV 行的可迭代对象。这意味着它们可以处理不同类型的输入源，而不仅仅是由文件名指定的文件。
2. 我们重新实现了 `read_csv_as_dicts()` 和 `read_csv_as_instances()` 函数，以使用这些新函数。这样，通过文件名从文件中读取数据的原始功能仍然可用，但现在它是基于更灵活的函数构建的。
3. 这种方法保持了与现有代码的向后兼容性。这意味着任何使用旧函数的代码仍然可以按预期工作。同时，我们的库变得更加灵活，因为它现在可以处理不同类型的输入源。
4. 现在，让我们测试这些新函数。创建一个名为 `test_reader_flexibility.py` 的文件，并添加以下代码。这段代码将使用不同类型的输入源来测试新函数：

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. 创建测试文件后，我们需要从终端运行测试脚本。打开终端，导航到 `test_reader_flexibility.py` 文件所在的目录。然后运行以下命令：

```bash
python test_reader_flexibility.py
```

输出应该类似于以下内容：

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

这个输出证实了我们的函数现在可以处理不同类型的输入源，同时保持了向后兼容性。重构后的函数可以处理来自以下数据源的数据：

- 使用 `open()` 打开的普通文件
- 使用 `gzip.open()` 打开的压缩文件
- 任何其他能产生文本行的可迭代对象

这使得我们的代码更加灵活，并且更容易在不同的场景中使用。
