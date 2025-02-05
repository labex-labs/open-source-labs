# 使用高阶函数

目前，`reader.py` 程序包含两个核心函数，`csv_as_dicts()` 和 `csv_as_instances()`。这两个函数中的代码几乎完全相同。例如：

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    将 CSV 数据行转换为字典列表
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, *, headers=None):
    '''
    将 CSV 数据行转换为实例列表
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
```

将这些函数的核心统一到一个名为 `convert_csv()` 的单一函数中，该函数接受一个用户定义的转换函数作为参数。例如：

```python
>>> def make_dict(headers, row):
        return dict(zip(headers, row))

>>> lines = open('portfolio.csv')
>>> convert_csv(lines, make_dict)
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'},
 {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'},
 {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'},
 {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

根据新的 `convert_csv()` 函数重写 `csv_as_dicts()` 和 `csv_as_instances()` 函数。
