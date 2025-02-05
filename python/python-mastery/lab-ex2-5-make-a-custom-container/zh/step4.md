# 创建一个自定义容器——巧妙的伪装

将数据存储为列形式能显著节省内存，但现在处理这些数据会变得相当麻烦。实际上，我们在练习2.2中编写的早期分析代码都无法处理列形式的数据。所有代码都无法正常运行的原因是，你打破了早期练习中使用的数据抽象——即数据存储为字典列表的假设。

如果你愿意创建一个自定义容器对象来“伪装”数据，这个问题就能得到解决。让我们来实现它。

早期的分析代码假设数据存储在一系列记录中。每个记录都表示为一个字典。我们先创建一个新的“序列”类。在这个类中，我们存储 `read_rides_as_columns()` 函数中使用的四列数据。

```python
# readrides.py

from collections.abc import Sequence

...

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # 列
        self.dates = []
        self.daytypes = []
        self.numrides = []
```

尝试创建一个 `RideData` 实例。你会发现它会因如下错误信息而失败：

```python
>>> records = RideData()
Traceback (most recent call last):
...
TypeError: Can't instantiate abstract class RideData with abstract methods __getitem__, __len__
>>>
```

仔细阅读错误信息。它告诉了我们需要实现的内容。让我们添加一个 `__len__()` 和 `__getitem__()` 方法。在 `__getitem__()` 方法中，我们将创建一个字典。此外，我们还将创建一个 `append()` 方法，该方法接受一个字典，并将其解包为四个单独的 `append()` 操作。

```python
# readrides.py
...

class RideData(collections.Sequence):
    def __init__(self):
        # 每个值都是一个包含所有值的列表（一列）
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # 假设所有列表长度相同
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

如果你操作正确，应该能够将这个对象放入之前编写的 `read_rides_as_dicts()` 函数中。这只需要更改一行代码：

```python
# readrides.py
...

def read_rides_as_dicts(filename):
    '''
    将公交出行数据读取为字典列表
    '''
    records = RideData()      # <--- 更改此处
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # 跳过标题行
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records
```

如果你操作正确，旧代码应该能像以前一样正常运行。例如：

```python
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> rows[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> rows[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> rows[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

运行你在练习2.2中编写的早期CTA代码。它应该无需修改就能正常运行，但使用的内存会大幅减少。
