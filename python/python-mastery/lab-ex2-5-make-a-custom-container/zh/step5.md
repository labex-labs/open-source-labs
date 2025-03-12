# 增强自定义容器的切片功能

我们的自定义容器在访问单个记录方面表现出色。然而，在进行切片操作时会出现问题。当你尝试对我们的容器进行切片时，结果并非你通常所期望的那样。

让我们来了解一下为什么会出现这种情况。在 Python 中，切片是一种常用的操作，用于提取序列的一部分。但对于我们的自定义容器，Python 不知道如何仅使用切片后的数据创建一个新的 `RideData` 对象。相反，它会创建一个列表，其中包含对切片中每个索引调用 `__getitem__` 方法的结果。

1. 让我们在 Python shell 中测试切片操作：

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

在这段代码中，我们首先导入 `readrides` 模块。然后将 `ctabus.csv` 文件中的数据读取到变量 `rows` 中。当我们尝试对前 10 条记录进行切片并检查结果的类型时，会发现它是一个列表，而不是 `RideData` 对象。打印结果可能会显示一些意外的内容，比如一个数字列表，而不是字典。

2. 让我们修改 `RideData` 类，使其能够正确处理切片操作。打开 `readrides.py` 文件并更新 `__getitem__` 方法：

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

在这个更新后的 `__getitem__` 方法中，我们首先检查 `index` 是否为切片对象。如果是，我们创建一个名为 `result` 的新 `RideData` 对象。然后，我们用原始数据列（`routes`、`dates`、`daytypes` 和 `numrides`）的切片来填充这个新对象。这样可以确保当我们对自定义容器进行切片时，得到的是另一个 `RideData` 对象，而不是一个列表。如果 `index` 不是切片对象（即它是一个单个索引），我们返回一个包含相关记录的字典。

3. 让我们测试改进后的切片功能：

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

在更新 `__getitem__` 方法后，我们可以再次测试切片操作。当我们对前 10 条记录进行切片时，结果的类型现在应该是 `readrides.RideData`。切片的长度应该是 10，并且访问切片中的单个元素应该得到与访问原始容器中相应元素相同的结果。

4. 你还可以使用不同的切片模式进行测试：

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

在这里，我们测试了不同的切片模式。第一个切片 `rows[0:20:2]` 获取前 20 条记录中的每隔一条记录，结果切片的长度应该是 10。第二个切片 `rows[-10:]` 获取最后 10 条记录，其长度也应该是 10。

通过正确实现切片功能，我们的自定义容器现在的行为更像一个标准的 Python 列表，同时保持了列向存储的内存效率。

这种创建自定义容器类的方法，即模仿 Python 内置容器但具有不同的内部表示，是一种强大的技术，可以在不改变代码向用户呈现的接口的情况下优化内存使用。
