# 准备工作

在练习2.6中，你编写了一个名为`reader.py`的模块，其中有一个用于将CSV文件读取为字典列表的函数。例如：

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>>
```

后来在练习3.3中，我们对该代码进行了扩展，使其能够处理实例：

```python
>>> import reader
>>> from stock import Stock
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```

最终，在练习3.7中，代码被重构为一个涉及继承的类集合。然而，代码已经变得相当复杂和混乱。
