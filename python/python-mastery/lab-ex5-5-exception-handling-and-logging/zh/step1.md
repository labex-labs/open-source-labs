# 准备工作

在`reader.py`文件中，有一个核心函数`convert_csv()`，它承担了大部分工作。如果你在包含缺失或错误数据的数据上运行此函数，它将会崩溃。例如：

```bash
$ python
>>> from reader import read_csv_as_dicts
```

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
回溯（最近一次调用）：
  文件 "<stdin>"，第1行，在 <模块> 中
  文件 "reader.py"，第24行，在 read_csv_as_dicts 中
    return csv_as_dicts(file, types, headers=headers)
  文件 "reader.py"，第13行，在 csv_as_dicts 中
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
  文件 "reader.py"，第9行，在 convert_csv 中
    return list(map(lambda row: converter(headers, row), rows))
  文件 "reader.py"，第9行，在 <lambda> 中
    return list(map(lambda row: converter(headers, row), rows))
  文件 "reader.py"，第13行，在 <lambda> 中
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
  文件 "reader.py"，第13行，在 <dictcomp> 中
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
值错误：基数为10的int()的无效文字：''
>>>
```
