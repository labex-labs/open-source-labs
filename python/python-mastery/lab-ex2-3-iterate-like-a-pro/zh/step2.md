# 使用 `enumerate()` 和 `zip()` 函数

在这一步中，我们将探索 Python 中两个非常有用的内置函数，它们对于迭代操作至关重要：`enumerate()` 和 `zip()`。当你处理序列时，这些函数可以显著简化你的代码。

## 使用 `enumerate()` 进行计数

当你遍历一个序列时，你可能经常需要跟踪每个元素的索引或位置。这时，`enumerate()` 函数就派上用场了。`enumerate()` 函数接受一个序列作为输入，并为该序列中的每个元素返回 (索引，值) 对。

如果你在上一步的 Python 解释器中继续操作，可以直接使用。如果没有，请开启一个新的会话。如果你要重新开始，可以按以下方式设置数据：

```python
# If you're starting a new session, reload the data first:
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Use enumerate to get row numbers
for rowno, row in enumerate(rows):
    print(rowno, row)
```

当你运行上述代码时，`enumerate(rows)` 函数会生成索引（从 0 开始）和 `rows` 序列中对应行的对。然后，`for` 循环将这些对解包到变量 `rowno` 和 `row` 中，并将它们打印出来。

输出：

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

我们可以通过将 `enumerate()` 与解包结合使用，让代码更具可读性。解包允许我们直接将序列的元素分配给各个变量。

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

在这段代码中，我们在 `(name, shares, price)` 周围使用了额外的一对括号，以正确解包行数据。`enumerate(rows)` 仍然为我们提供索引和行，但现在我们将行解包到 `name`、`shares` 和 `price` 变量中。

输出：

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

## 使用 `zip()` 配对数据

`zip()` 函数是 Python 中的另一个强大工具。它用于组合多个序列中对应的元素。当你将多个序列传递给 `zip()` 时，它会创建一个迭代器，生成元组，每个元组包含输入序列中相同位置的元素。

让我们看看如何将 `zip()` 与我们一直在处理的 `headers` 和 `row` 数据结合使用。

```python
# Recall the headers variable from earlier
print(headers)  # Should show ['name', 'shares', 'price']

# Get the first row
row = rows[0]
print(row)      # Should show ['AA', '100', '32.20']

# Use zip to pair column names with values
for col, val in zip(headers, row):
    print(col, val)
```

在这段代码中，`zip(headers, row)` 接受 `headers` 序列和 `row` 序列，并将它们对应的元素配对。然后，`for` 循环将这些对解包到 `col`（用于 `headers` 中的列名）和 `val`（用于 `row` 中的值）中，并将它们打印出来。

输出：

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

`zip()` 的一个非常常见的用途是从键值对创建字典。在 Python 中，字典是键值对的集合。

```python
# Create a dictionary from headers and row values
record = dict(zip(headers, row))
print(record)
```

在这里，`zip(headers, row)` 创建列名和值的对，`dict()` 函数将这些对转换为字典。

输出：

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

我们可以扩展这个想法，将 `rows` 序列中的所有行转换为字典。

```python
# Convert all rows to dictionaries
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

在这个循环中，对于 `rows` 中的每一行，我们使用 `zip(headers, row)` 创建键值对，然后使用 `dict()` 将这些对转换为字典。这种技术在数据处理应用中非常常见，特别是在处理第一行包含标题的 CSV 文件时。

输出：

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```
