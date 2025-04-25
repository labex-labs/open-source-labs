# 练习 3.3：读取 CSV 文件

首先，让我们专注于将 CSV 文件读取为字典列表的问题。在 `fileparse_3.3.py` 文件中，定义一个如下所示的函数：

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    将 CSV 文件解析为记录列表
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # 读取文件头
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # 跳过无数据的行
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

此函数将 CSV 文件读取为字典列表，同时隐藏了打开文件、用 `csv` 模块包装它、忽略空行等细节。

试试看：

提示：`python3 -i fileparse_3.3.py`。

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

这样很好，只是你无法对这些数据进行任何有用的计算，因为所有内容都表示为字符串。我们很快会解决这个问题，但让我们继续在此基础上构建。
