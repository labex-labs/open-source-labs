# 改变你的数据方向（转为列形式）

如果你改变对数据的看法，通常可以节省大量内存。例如，如果你使用这个函数将所有公交数据读入列中会发生什么？

```python
# readrides.py

...

def read_rides_as_columns(filename):
    '''
    将公交出行数据读入4个列表，分别代表各列
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # 跳过标题行
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

从理论上讲，这个函数应该能节省大量内存。在尝试之前让我们分析一下。

首先，数据文件包含577563行数据，每行包含四个值。如果每行存储为一个字典，那么这些字典的最小大小为240字节。

```python
>>> nrows = 577563     # 原始文件中的行数
>>> nrows * 240
138615120
>>>
```

所以，仅字典本身就需要138MB。这还不包括实际存储在字典中的任何值。

通过转为列形式，数据存储在4个单独的列表中。每个列表中每个项存储一个指针需要8字节。所以，这里对列表所需内存有一个粗略估计：

```python
>>> nrows * 4 * 8
18482016
>>>
```

这大约是18MB的列表开销。所以，转为列形式仅通过消除所有需要存储在字典中的额外信息，就应该能节省大约120MB的内存。

尝试使用这个函数读取公交数据并查看内存使用情况。

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> columns = read_rides_as_columns('ctabus.csv')
>>> tracemalloc.get_traced_memory()
...查看结果...
>>>
```

结果是否反映了我们上面粗略计算中预期的内存节省情况？
