# 创建自定义容器类

在数据处理中，列向存储方法在节省内存方面表现出色。然而，当你现有的代码期望数据以字典列表的形式存在时，这种方法可能会引发问题。为了解决这个问题，我们将创建一个自定义容器类。这个类将呈现行向的接口，这意味着在你的代码看来，它的外观和行为就像一个字典列表。但在内部，它将以列向格式存储数据，从而帮助我们节省内存。

1. 首先，在 WebIDE 编辑器中打开 `readrides.py` 文件。我们将向这个文件中添加一个新的类。这个类将成为我们自定义容器的基础。

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

在这段代码中，我们定义了一个名为 `RideData` 的类，它继承自 `Sequence`。`__init__` 方法初始化了四个空列表，每个列表代表一列数据。`__len__` 方法返回容器的长度，该长度与 `routes` 列表的长度相同。`__getitem__` 方法允许我们通过索引访问特定的记录，并将其作为字典返回。`append` 方法通过将值追加到每列的列表中，向容器中添加一条新记录。

2. 现在，我们需要一个函数将公交乘车数据读取到我们的自定义容器中。将以下函数添加到 `readrides.py` 文件中。

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

这个函数创建了一个 `RideData` 类的实例，并使用 CSV 文件中的数据填充它。它从文件中读取每一行，提取相关信息，为每条记录创建一个字典，然后将其追加到 `RideData` 容器中。关键在于，它保持了与字典列表相同的接口，但在内部以列的形式存储数据。

3. 让我们在 Python shell 中测试我们的自定义容器。这将帮助我们验证它是否按预期工作。

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

我们的自定义容器成功实现了 `Sequence` 接口，这意味着它的行为类似于列表。你可以使用 `len()` 函数获取容器中记录的数量，也可以使用索引访问单个记录。每条记录看起来都是一个字典，尽管数据在内部是以列的形式存储的。这很棒，因为期望使用字典列表的现有代码可以直接与我们的自定义容器一起使用，而无需进行任何修改。

4. 最后，让我们测量一下自定义容器的内存使用情况。这将向我们展示与字典列表相比，我们节省了多少内存。

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

当你运行这段代码时，你应该会看到内存使用情况与列向存储方法相似，远低于使用字典列表的情况。这展示了我们的自定义容器在内存效率方面的优势。
