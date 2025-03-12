# 处理字典和 CSV 数据

让我们从研究一个关于股票持仓的简单数据集开始。在这一步中，你将学习如何从 CSV 文件中读取数据，并使用字典将其存储为结构化格式。

CSV（逗号分隔值）文件是存储表格数据的常用方式，其中每行代表一行数据，值之间用逗号分隔。Python 中的字典是一种强大的数据结构，允许你存储键值对。通过使用字典，我们可以以更有意义的方式组织 CSV 文件中的数据。

首先，按照以下步骤在 WebIDE 中创建一个新的 Python 文件：

1. 点击 WebIDE 中的“New File”按钮。
2. 将文件命名为 `readport.py`。
3. 将以下代码复制并粘贴到文件中：

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

这段代码定义了一个 `read_portfolio` 函数，它执行了几个重要的任务：

1. 它打开由 `filename` 参数指定的 CSV 文件。`open` 函数用于访问文件，`with` 语句确保在我们读取完文件后正确关闭文件。
2. 它跳过标题行。标题行通常包含 CSV 文件中各列的名称。我们使用 `next(rows)` 将迭代器移动到下一行，从而跳过标题行。
3. 对于每一行数据，它创建一个字典。字典的键为 'name'、'shares' 和 'price'。这些键将帮助我们以更直观的方式访问数据。
4. 它将股票数量转换为整数，将价格转换为浮点数。这很重要，因为从 CSV 文件中读取的数据最初是字符串格式，而我们需要数值进行计算。
5. 它将每个字典添加到一个名为 `portfolio` 的列表中。这个列表将包含 CSV 文件中的所有记录。
6. 最后，它返回完整的字典列表。

现在，让我们为公交数据创建一个文件。创建一个名为 `readrides.py` 的新文件，内容如下：

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

这个 `read_rides_as_dicts` 函数的工作方式与 `read_portfolio` 函数类似。它读取与芝加哥交通管理局（CTA）公交数据相关的 CSV 文件，跳过标题行，为每一行数据创建一个字典，并将这些字典存储在一个列表中。

现在，让我们通过在 WebIDE 中打开一个终端来测试 `read_portfolio` 函数：

1. 点击“Terminal”菜单并选择“New Terminal”。
2. 输入 `python3` 启动 Python 解释器。
3. 执行以下命令：

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

这里使用了 `pprint` 函数（漂亮打印）以更易读的格式显示数据。列表中的每个项都是一个表示一笔股票持仓的字典。字典有以下键：

- 股票代码 (`name`)：这是用于识别股票的缩写。
- 持有股票数量 (`shares`)：这表示持有的该股票的股数。
- 每股购买价格 (`price`)：这是每股的购买价格。

注意，像 'MSFT' 和 'IBM' 这样的股票出现了多次。这些代表了对同一只股票的不同购买，可能是在不同时间和以不同价格进行的。
