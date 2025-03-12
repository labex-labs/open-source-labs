# 创建用于 CSV 处理的实用函数

既然我们已经了解了 Python 的一等对象如何帮助我们进行数据转换，接下来我们将创建一个可复用的实用函数。这个函数将读取 CSV 数据并将其转换为字典列表。这是一个非常有用的操作，因为 CSV 文件通常用于存储表格数据，将其转换为字典列表可以让我们在 Python 中更轻松地处理这些数据。

## 创建 CSV 读取器实用函数

首先，打开 WebIDE。打开后，导航到项目目录并创建一个名为 `reader.py` 的新文件。在这个文件中，我们将定义一个读取 CSV 数据并进行类型转换的函数。类型转换很重要，因为 CSV 文件中的数据通常以字符串形式读取，但我们可能需要不同的数据类型（如整数或浮点数）进行进一步处理。

将以下代码添加到 `reader.py` 中：

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dictionaries, converting each field according
    to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    list: List of dictionaries representing the CSV data
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        for row in rows:
            # Apply type conversions to each value in the row
            converted_row = [func(val) for func, val in zip(types, row)]

            # Create a dictionary mapping headers to converted values
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

这个函数首先打开指定的 CSV 文件，然后读取 CSV 文件的表头（即列名）。接着，它会遍历文件中的每一行。对于行中的每个值，它会应用 `types` 列表中对应的类型转换函数。最后，它会创建一个字典，其中键是列名，值是转换后的数据，并将这个字典添加到 `records` 列表中。处理完所有行后，它会返回 `records` 列表。

## 测试实用函数

让我们来测试一下我们的实用函数。首先，打开一个终端并输入以下命令启动 Python 解释器：

```bash
python3
```

现在我们已经进入了 Python 解释器，可以使用我们的函数来读取投资组合（portfolio）数据。投资组合数据是一个 CSV 文件，包含股票信息，如股票名称、股数和价格。

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

当你运行这段代码时，你应该会看到类似于以下的输出：

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

这个输出显示了投资组合数据中的前三条记录，并且数据类型已经正确转换。

让我们再用芝加哥交通管理局（CTA）的公交数据来测试一下我们的函数。CTA 公交数据是另一个 CSV 文件，包含公交线路、日期、工作日类型和乘车人数等信息。

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

输出应该类似于：

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

这表明我们的函数可以处理不同的 CSV 文件并进行适当的类型转换。

要退出 Python 解释器，请输入：

```python
exit()
```

现在你已经创建了一个可复用的实用函数，它可以读取任何 CSV 文件并进行适当的类型转换。这展示了 Python 一等对象的强大之处，以及如何利用它们来创建灵活、可复用的代码。
