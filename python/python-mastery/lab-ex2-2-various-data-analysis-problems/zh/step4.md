# 芝加哥交通管理局数据的数据分析挑战

既然你已经练习了使用不同的 Python 数据结构和 `collections` 模块，现在是时候将这些技能应用到实际的数据分析任务中了。在这个实验中，我们将分析芝加哥交通管理局（CTA）的公交乘客数据。这个实际应用将帮助你理解如何使用 Python 从真实世界的数据集中提取有意义的信息。

## 理解数据

首先，让我们看看我们要处理的交通数据。在你的 Python 终端中，你将运行一些代码来加载数据并了解其基本结构。

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

`import readrides` 语句导入了一个自定义模块，该模块有一个从 CSV 文件读取数据的函数。`readrides.read_rides_as_dicts` 函数从指定的 CSV 文件中读取数据，并将每一行转换为一个字典。`len(rows)` 给出了数据集中记录的总数。通过使用 `pprint.pprint(rows[0])` 打印第一条记录，我们可以清楚地看到每条记录的结构。

数据包含不同公交线路的每日乘客记录。每条记录包括：

- `route`：公交线路编号
- `date`：日期，格式为 "YYYY - MM - DD"
- `daytype`："W" 表示工作日，"A" 表示周六，"U" 表示周日/节假日
- `rides`：当天的乘客数量

## 分析任务

让我们逐个解决这些挑战问题：

### 问题 1：芝加哥有多少条公交线路？

要回答这个问题，我们需要找出数据集中所有唯一的线路编号。我们将使用集合推导式来完成这个任务。

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

集合推导式是一种简洁的创建集合的方式。在这种情况下，我们遍历 `rows` 列表中的每一行，并提取 `route` 值。由于集合只存储唯一元素，我们最终得到一个包含所有唯一线路编号的集合。打印这个集合的长度，就得到了唯一公交线路的总数。

我们还可以查看其中一些线路编号：

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

在这里，我们将唯一线路的集合转换为列表，然后打印该列表的前 10 个元素。

### 问题 2：2011 年 2 月 2 日，22 路公交车有多少乘客？

对于这个问题，我们需要过滤数据，找到与给定线路和日期匹配的特定记录。

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

我们首先定义 `target_date` 和 `target_route` 变量。然后，我们遍历 `rows` 列表中的每一行。对于每一行，我们检查 `route` 和 `date` 是否与我们的目标值匹配。如果找到匹配项，我们打印乘客数量并跳出循环，因为我们已经找到了我们要找的记录。

你可以通过更改 `target_date` 和 `target_route` 变量来检查任何日期的任何线路。

### 问题 3：每条公交线路的总乘客数是多少？

让我们使用 `Counter` 来计算每条线路的总乘客数。`Counter` 是 `collections` 模块中的一个字典子类，用于对可哈希对象进行计数。

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

我们首先从 `collections` 模块导入 `Counter` 类。然后，我们初始化一个名为 `total_rides_by_route` 的空计数器。当我们遍历 `rows` 列表中的每一行时，我们将每条线路的乘客数量添加到计数器中。最后，我们使用 `most_common(5)` 方法获取总乘客数最高的前 5 条线路，并打印结果。

### 问题 4：哪五条公交线路在 2001 年至 2011 年期间乘客数量增长最多？

这是一个更复杂的任务。我们需要比较每条线路在 2001 年和 2011 年的乘客数量。

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

我们首先创建两个 `Counter` 对象 `rides_2001` 和 `rides_2011`，分别存储 2001 年和 2011 年每条线路的总乘客数。当我们遍历 `rows` 列表中的每一行时，我们检查日期是否以 '2001 -' 或 '2011 -' 开头，并将乘客数添加到相应的计数器中。

然后，我们创建一个空字典 `increases` 来存储每条线路的乘客增长数量。我们遍历唯一线路，通过从 2011 年的乘客数中减去 2001 年的乘客数来计算增长数量。

为了找到增长最多的前 5 条线路，我们使用 `heapq.nlargest` 函数。这个函数接受要返回的元素数量（这里是 5）、可迭代对象（`increases.items()`）和一个键函数（`lambda x: x[1]`），该键函数指定了如何比较元素。

最后，我们打印结果，显示线路编号、乘客增长数量以及 2001 年和 2011 年的乘客数量。

这个分析确定了哪些公交线路在这十年中乘客数量增长最多，这可能表明人口模式的变化、服务的改善或其他有趣的趋势。

你可以通过多种方式扩展这些分析。例如，你可能想要：

- 按星期几分析乘客模式
- 找出乘客数量下降的线路
- 比较乘客数量的季节性变化

你在这个实验中学到的技术为这种数据探索和分析提供了坚实的基础。
