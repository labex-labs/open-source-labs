# 基本迭代和序列解包

在这一步中，我们将探索使用 `for` 循环进行基本迭代以及 Python 中的序列解包。迭代是编程中的一个基本概念，它允许你逐个遍历序列中的每个元素。而序列解包则能让你以一种便捷的方式将序列中的单个元素赋值给变量。

## 从 CSV 文件加载数据

让我们从从 CSV 文件加载一些数据开始。CSV（逗号分隔值）是一种用于存储表格数据的常见文件格式。首先，你需要在 WebIDE 中打开一个终端并启动 Python 解释器。这样你就可以交互式地运行 Python 代码。

```bash
cd ~/project
python3
```

现在你已经进入了 Python 解释器，可以执行以下 Python 代码来从 `portfolio.csv` 文件中读取数据。首先，我们导入 `csv` 模块，它提供了处理 CSV 文件的功能。然后，我们打开文件并创建一个 `csv.reader` 对象来读取数据。我们使用 `next` 函数获取列标题，并将剩余的数据转换为列表。最后，我们使用 `pprint` 模块中的 `pprint` 函数以更易读的格式打印行。

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Get the column headers
rows = list(f_csv)       # Convert the remaining data to a list
from pprint import pprint
pprint(rows)             # Pretty print the rows
```

你应该会看到类似以下的输出：

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## 使用 `for` 循环进行基本迭代

Python 中的 `for` 语句用于遍历任何数据序列，如列表、元组或字符串。在我们的例子中，我们将使用它来遍历从 CSV 文件加载的数据行。

```python
for row in rows:
    print(row)
```

这段代码将遍历 `rows` 列表中的每一行并打印出来。你会看到 CSV 文件中的每一行数据逐个打印出来。

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## 循环中的序列解包

Python 允许你在 `for` 循环中直接解包序列。当你知道序列中每个元素的结构时，这非常有用。在我们的例子中，`rows` 列表中的每一行包含三个元素：名称、股票数量和价格。我们可以在 `for` 循环中直接解包这些元素。

```python
for name, shares, price in rows:
    print(name, shares, price)
```

这段代码将把每一行解包到变量 `name`、`shares` 和 `price` 中，然后打印出来。你会看到数据以更易读的格式打印出来。

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

如果你不需要某些值，可以使用 `_` 作为占位符来表示你不关心这些值。例如，如果你只想打印名称和价格，可以使用以下代码：

```python
for name, _, price in rows:
    print(name, price)
```

这段代码将忽略每一行中的第二个元素，只打印名称和价格。

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## 使用 `*` 运算符进行扩展解包

对于更高级的解包，你可以使用 `*` 运算符作为通配符。这允许你将多个元素收集到一个列表中。让我们使用这种技术按名称对数据进行分组。

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Print the data for IBM
print(byname['IBM'])

# Iterate through IBM's data
for shares, price in byname['IBM']:
    print(shares, price)
```

在这段代码中，我们首先从 `collections` 模块导入 `defaultdict` 类。`defaultdict` 是一种字典，如果键不存在，它会自动创建一个新值（在这种情况下是一个空列表）。然后，我们使用 `*` 运算符将除第一个元素之外的所有元素收集到一个名为 `data` 的列表中。我们将这个列表存储在 `byname` 字典中，按名称分组。最后，我们打印 IBM 的数据并遍历它以打印股票数量和价格。

输出：

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 70.44
```

在这个例子中，`*data` 将除第一个元素之外的所有元素收集到一个列表中，然后我们将其存储在按名称分组的字典中。这是一种处理可变长度序列数据的强大技术。
