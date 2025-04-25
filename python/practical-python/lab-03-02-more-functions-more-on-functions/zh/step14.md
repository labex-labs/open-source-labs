# 练习 3.4：构建列选择器

在许多情况下，你只对 CSV 文件中的某些特定列感兴趣，而不是所有数据。修改 `parse_csv()` 函数，使其可以根据用户指定，有选择地提取列数据，如下所示：

```python
>>> # 读取所有数据
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]

>>> # 仅读取部分数据
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA','shares': '100'}, {'name': 'IBM','shares': '50'}, {'name': 'CAT','shares': '150'}, {'name': 'MSFT','shares': '200'}, {'name': 'GE','shares': '95'}, {'name': 'MSFT','shares': '50'}, {'name': 'IBM','shares': '100'}]
>>>
```

在练习 2.23 中给出了一个列选择器的示例。不过，这里有一种实现方法：

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    将 CSV 文件解析为记录列表
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # 读取文件头
        headers = next(rows)

        # 如果提供了列选择器，找到指定列的索引。
        # 同时缩小用于生成结果字典的标题集
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # 跳过无数据的行
                continue
            # 如果选择了特定列，则过滤该行
            if indices:
                row = [ row[index] for index in indices ]

            # 创建字典
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

这部分有一些棘手的地方。可能最重要的一点是将列选择映射到行索引。例如，假设输入文件有以下标题：

```python
>>> headers = ['name', 'date', 'time','shares', 'price']
>>>
```

现在，假设选择的列如下：

```python
>>> select = ['name','shares']
>>>
```

为了进行正确的选择，你必须将所选列名映射到文件中的列索引。这就是这一步所做的事情：

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

换句话说，“name”是第 0 列，“shares”是第 3 列。当你从文件中读取一行数据时，这些索引用于过滤它：

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
