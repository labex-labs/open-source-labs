# 通用化

类方法的一个有用特性是，你可以使用它们为各种各样的类提供一个高度统一的实例创建接口，并编写使用这些接口的通用实用函数。

早些时候，你创建了一个 `reader.py` 文件，其中包含一些用于读取 CSV 数据的函数。向该文件中添加以下 `read_csv_as_instances()` 函数，该函数接受一个类作为输入，并使用类的 `from_row()` 方法创建一个实例列表：

```python
# reader.py
...

def read_csv_as_instances(filename, cls):
    '''
    将 CSV 文件读取为实例列表
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

删除 `read_portfolio()` 函数 —— 你不再需要它了。如果你想读取 `Stock` 对象列表，可以这样做：

```python
>>> # 读取 Stock 实例的投资组合
>>> from reader import read_csv_as_instances
>>> from stock import Stock
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[<__main__.Stock object at 0x100674748>,
<__main__.Stock object at 0x1006746d8>,
<__main__.Stock object at 0x1006747b8>,
<__main__.Stock object at 0x100674828>,
<__main__.Stock object at 0x100674898>,
<__main__.Stock object at 0x100674908>,
<__main__.Stock object at 0x100674978>]
>>>
```

以下是另一个如何将 `read_csv_as_instances()` 与完全不同的类一起使用的示例：

```python
>>> class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

>>> rides = read_csv_as_instances('ctabus.csv', Row)
>>> len(rides)
577563
>>>
```

**讨论**

本实验说明了类变量和类方法的两种最常见用法。类变量通常用于保存全局参数（例如，配置设置），该参数在所有实例之间共享。有时子类会从基类继承并覆盖该设置以更改行为。

类方法最常用于实现如前所示的替代构造函数。识别此类类方法的一种常见方法是在名称中查找 “from” 一词。例如，以下是内置字典的一个示例：

```python
>>> d = dict.fromkeys(['a','b','c'], 0)     # 类方法
>>> d
{'a': 0, 'c': 0, 'b': 0}
>>>
```
