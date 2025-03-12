# 创建高阶函数

在 Python 中，高阶函数是可以接受另一个函数作为参数的函数。这能带来更高的灵活性和代码复用性。现在，让我们创建一个名为 `convert_csv()` 的高阶函数。这个函数将处理处理 CSV 数据的常见操作，同时允许你自定义如何将 CSV 的每一行转换为一条记录。

在 WebIDE 中打开 `reader.py` 文件。我们将添加一个函数，该函数将接受一个 CSV 数据的可迭代对象、一个转换函数，还可以选择传入列名。转换函数将用于把 CSV 的每一行转换为一条记录。

以下是 `convert_csv()` 函数的代码。将其复制并粘贴到你的 `reader.py` 文件中：

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

让我们来详细分析这个函数的功能。首先，它初始化一个名为 `records` 的空列表，用于存储转换后的记录。然后，它使用 `csv.reader()` 函数读取 CSV 数据行。如果没有提供列名，它会将第一行作为列名。对于后续的每一行，它会应用 `conversion_func` 函数将该行转换为一条记录，并将其添加到 `records` 列表中。最后，它返回记录列表。

现在，我们需要一个简单的转换函数来测试我们的 `convert_csv()` 函数。这个函数将接受列名和一行数据，并使用列名作为键将该行转换为一个字典。

以下是 `make_dict()` 函数的代码。也将这个函数添加到你的 `reader.py` 文件中：

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

`make_dict()` 函数使用 `zip()` 函数将每个列名与该行中对应的数值配对，然后从这些配对中创建一个字典。

让我们来测试这些函数。在终端中运行以下命令来打开一个 Python 交互式 shell：

```bash
cd ~/project
python3 -i reader.py
```

`python3` 命令中的 `-i` 选项以交互模式启动 Python 解释器，并导入 `reader.py` 文件，这样我们就可以使用刚刚定义的函数。

在 Python shell 中，运行以下代码来测试我们的函数：

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

这段代码打开 `portfolio.csv` 文件，使用 `convert_csv()` 函数和 `make_dict()` 转换函数将 CSV 数据转换为字典列表，然后打印结果。

你应该会看到类似于以下的输出：

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

这个输出表明我们的高阶函数 `convert_csv()` 正常工作。我们成功创建了一个接受另一个函数作为参数的函数，这使我们能够轻松改变 CSV 数据的转换方式。

要退出 Python shell，你可以输入 `exit()` 或按 Ctrl+D。
