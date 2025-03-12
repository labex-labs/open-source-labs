# 创建基本的 CSV 读取函数

让我们先创建一个 `reader.py` 文件，其中包含两个用于读取 CSV 数据的基本函数。这些函数将帮助我们以不同的方式处理 CSV 文件，例如将数据转换为字典或类实例。

首先，我们需要了解什么是 CSV 文件。CSV 代表逗号分隔值（Comma-Separated Values）。它是一种用于存储表格数据的简单文件格式，其中每行代表一行数据，每行中的值用逗号分隔。

现在，让我们创建 `reader.py` 文件。按照以下步骤操作：

1. 打开代码编辑器，在 `/home/labex/project` 目录下创建一个名为 `reader.py` 的新文件。我们将在这里编写读取 CSV 数据的函数。

2. 将以下代码添加到 `reader.py` 中：

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

在 `read_csv_as_dicts` 函数中，我们首先使用 `open` 函数打开 CSV 文件。然后，使用 `csv.reader` 逐行读取文件。`next(rows)` 语句读取文件的第一行，通常这一行包含表头。之后，我们遍历剩余的行。对于每一行，我们创建一个字典，其中键是表头，值是该行中对应的数值，并可选择使用 `types` 列表进行类型转换。

`read_csv_as_instances` 函数类似，但它不是创建字典，而是创建给定类的实例。它假设该类有一个名为 `from_row` 的静态方法，可以从一行数据创建一个实例。

3. 让我们测试这些函数，确保它们能正常工作。创建一个名为 `test_reader.py` 的新文件，并添加以下代码：

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

在 `test_reader.py` 文件中，我们导入刚刚创建的 `reader` 模块和 `stock` 模块。然后，通过使用一个名为 `portfolio.csv` 的示例 CSV 文件调用这两个函数来进行测试。我们打印投资组合中的第一个项目和项目总数，以验证函数是否按预期工作。

4. 从终端运行测试脚本：

```bash
python test_reader.py
```

输出应该类似于以下内容：

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

这证实了我们的两个函数工作正常。第一个函数将 CSV 数据转换为经过适当类型转换的字典列表，第二个函数使用提供的类的静态方法创建类实例。

下一步，我们将重构这些函数，使其更加灵活，允许它们处理任何可迭代的数据来源，而不仅仅是文件名。
