# 练习3.9：捕获异常

你编写的 `parse_csv()` 函数用于处理文件的全部内容。然而，在现实世界中，输入文件可能存在损坏、缺失或脏数据的情况。尝试这个实验：

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

修改 `parse_csv()` 函数，捕获在创建记录期间生成的所有 `ValueError` 异常，并为无法转换的行打印一条警告消息。

该消息应包括行号以及失败原因的相关信息。为了测试你的函数，尝试读取上面的 `missing.csv` 文件。例如：

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
第4行：无法转换 ['MSFT', '', '51.23']
第4行：原因是int() 无法将空字符串转换为十进制整数
第7行：无法转换 ['IBM', '', '70.44']
第7行：原因是int() 无法将空字符串转换为十进制整数
>>>
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```
