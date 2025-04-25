# 练习 6.10：创建更多管道组件

让我们将整个概念扩展到一个更大的管道中。在一个单独的文件 `ticker.py` 中，首先创建一个像你上面那样读取 CSV 文件的函数：

```python
# ticker.py

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = follow('stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
```

编写一个新函数来选择特定的列：

    # ticker.py

...
def select_columns(rows, indices):
for row in rows:
yield [row[index] for index in indices]
...
def parse_stock_data(lines):
rows = csv.reader(lines)
rows = select_columns(rows, [0, 1, 4])
return rows

再次运行你的程序。你应该会看到输出被精简成这样：

    ['GOOG', '1503.06', '2.81']
    ['AAPL', '253.31', '2.81']
    ['GOOG', '1503.07', '2.82']
    ['AAPL', '253.32', '2.82']
    ['GOOG', '1503.08', '2.83']

...

编写生成器函数来转换数据类型并构建字典。例如：

```python
# ticker.py
...

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
...
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
...
```

再次运行你的程序。现在你应该会得到这样一连串的字典：

    {'name': 'GOOG', 'price': 1503.4, 'change': 3.15}
    {'name': 'AAPL', 'price': 253.65, 'change': 3.15}
    {'name': 'GOOG', 'price': 1503.41, 'change': 3.16}
    {'name': 'AAPL', 'price': 253.66, 'change': 3.16}
    {'name': 'GOOG', 'price': 1503.42, 'change': 3.17}
    {'name': 'AAPL', 'price': 253.67, 'change': 3.17}

...
