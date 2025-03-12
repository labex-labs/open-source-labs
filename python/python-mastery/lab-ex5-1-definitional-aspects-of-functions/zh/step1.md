# 理解上下文

在之前的练习中，你可能遇到过读取 CSV 文件并将数据存储在各种数据结构中的代码。这段代码的目的是从 CSV 文件中获取原始文本数据，并将其转换为更有用的 Python 对象，如字典或类实例。这种转换至关重要，因为它使我们能够在 Python 程序中以更结构化、更有意义的方式处理数据。

读取 CSV 文件的典型模式通常遵循特定的结构。以下是一个读取 CSV 文件并将每行转换为字典的函数示例：

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

让我们来详细分析这个函数的工作原理。首先，它导入了 `csv` 模块，该模块为 Python 处理 CSV 文件提供了功能。该函数接受两个参数：`filename`，即要读取的 CSV 文件的名称；`types`，这是一个函数列表，用于将每列的数据转换为适当的数据类型。

在函数内部，它初始化了一个名为 `records` 的空列表，用于存储表示 CSV 文件每行的字典。然后，它使用 `with` 语句打开文件，这确保了在代码块执行完毕后文件会被正确关闭。`csv.reader` 函数用于创建一个迭代器，用于读取 CSV 文件的每一行。第一行被假定为表头，因此使用 `next` 函数获取。

接下来，函数遍历 CSV 文件中剩余的行。对于每一行，它使用字典推导式创建一个字典。字典的键是列名，值是将 `types` 列表中相应的类型转换函数应用于该行中的值的结果。最后，将该字典添加到 `records` 列表中，函数返回字典列表。

现在，让我们看一个类似的函数，它将 CSV 文件中的数据读取为类实例：

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

这个函数与前一个函数类似，但它不是创建字典，而是创建类的实例。该函数接受两个参数：`filename`，即要读取的 CSV 文件的名称；`cls`，即要创建其实例的类。

在函数内部，它遵循与前一个函数类似的结构。它初始化一个名为 `records` 的空列表，用于存储类实例。然后，它打开文件，读取表头，并遍历剩余的行。对于每一行，它调用类 `cls` 的 `from_row` 方法，使用该行的数据创建类的一个实例。然后将该实例添加到 `records` 列表中，函数返回实例列表。

在这个实验中，我们将重构这些函数，使其更加灵活和健壮。我们还将探索 Python 的类型提示（type hinting）系统，它允许我们指定函数参数和返回值的预期类型。这可以使我们的代码更具可读性，更易于理解，特别是对于可能使用我们代码的其他开发者来说。

让我们先创建一个 `reader.py` 文件，并将这些初始函数添加到其中。在进行下一步之前，请确保测试这些函数，以确保它们能正常工作。
