# 其他数据结构的内存使用情况

Python有许多不同的方式来表示数据结构。例如：

```python
# 一个元组
row = (route, date, daytype, rides)

# 一个字典
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# 一个类
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# 一个具名元组
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# 一个带有 __slots__ 的类
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
```

你的任务如下：创建不同版本的 `read_rides()` 函数，使用这些数据结构中的每一种来表示一行数据。然后，找出每种选项所产生的内存使用情况。如果你要一次性处理大量数据，找出哪种方法提供了最有效的存储方式。
