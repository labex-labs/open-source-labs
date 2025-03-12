# 比较不同的数据结构

在 Python 中，数据结构用于组织和存储相关数据。它们就像容器，以结构化的方式容纳不同类型的信息。在这一步中，我们将比较不同的数据结构，并了解它们的内存使用情况。

让我们在 `/home/labex/project` 目录下创建一个名为 `compare_structures.py` 的新文件。这个文件将包含从 CSV 文件中读取数据并将其存储在不同数据结构中的代码。

```python
# compare_structures.py
import csv
import tracemalloc
from collections import namedtuple

# 为出行数据定义一个命名元组
RideRecord = namedtuple('RideRecord', ['route', 'date', 'daytype', 'rides'])

# 命名元组是一种轻量级类，允许你通过名称访问其字段。
# 它类似于元组，但具有命名属性。

# 定义一个使用 __slots__ 进行内存优化的类
class SlottedRideRecord:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# 使用 __slots__ 的类是一种内存优化类。
# 它避免使用实例字典，从而节省内存。

# 为出行数据定义一个普通类
class RegularRideRecord:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# 普通类是一种面向对象的数据表示方式。
# 它具有命名属性，并且可以有方法。

# 以元组形式读取数据的函数
def read_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # 跳过标题行
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# 此函数从 CSV 文件中读取数据并将其存储为元组。
# 元组是不可变序列，你可以通过数字索引访问其元素。

# 以字典形式读取数据的函数
def read_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # 获取标题行
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            }
            records.append(record)
    return records

# 此函数从 CSV 文件中读取数据并将其存储为字典。
# 字典使用键值对，因此你可以通过名称访问元素。

# 以命名元组形式读取数据的函数
def read_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # 跳过标题行
        for row in rows:
            record = RideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# 此函数从 CSV 文件中读取数据并将其存储为命名元组。
# 命名元组结合了元组的效率和命名访问的可读性。

# 以普通类实例形式读取数据的函数
def read_as_regular_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # 跳过标题行
        for row in rows:
            record = RegularRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# 此函数从 CSV 文件中读取数据并将其存储为普通类的实例。
# 普通类允许你为数据添加方法。

# 以使用 __slots__ 的类实例形式读取数据的函数
def read_as_slotted_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # 跳过标题行
        for row in rows:
            record = SlottedRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# 此函数从 CSV 文件中读取数据并将其存储为使用 __slots__ 的类的实例。
# 使用 __slots__ 的类经过内存优化，并且仍然提供命名访问。

# 测量内存使用的函数
def measure_memory(func, filename):
    tracemalloc.start()

    records = func(filename)

    current, peak = tracemalloc.get_traced_memory()

    # 演示如何使用每种数据结构
    first_record = records[0]
    if func.__name__ == 'read_as_tuples':
        route, date, daytype, rides = first_record
    elif func.__name__ == 'read_as_dicts':
        route = first_record['route']
        date = first_record['date']
        daytype = first_record['daytype']
        rides = first_record['rides']
    else:  # 命名元组和类
        route = first_record.route
        date = first_record.date
        daytype = first_record.daytype
        rides = first_record.rides

    print(f"Structure type: {func.__name__}")
    print(f"Record count: {len(records)}")
    print(f"Example access: Route={route}, Date={date}, Rides={rides}")
    print(f"Current memory: {current/1024/1024:.2f} MB")
    print(f"Peak memory: {peak/1024/1024:.2f} MB")
    print("-" * 50)

    tracemalloc.stop()

    return current

if __name__ == "__main__":
    filename = '/home/labex/project/ctabus.csv'

    # 运行所有内存测试
    print("Memory usage comparison for different data structures:\n")

    results = []
    for reader_func in [
        read_as_tuples,
        read_as_dicts,
        read_as_named_tuples,
        read_as_regular_classes,
        read_as_slotted_classes
    ]:
        memory = measure_memory(reader_func, filename)
        results.append((reader_func.__name__, memory))

    # 按内存使用排序（从低到高）
    results.sort(key=lambda x: x[1])

    print("\nRanking by memory efficiency (most efficient first):")
    for i, (name, memory) in enumerate(results, 1):
        print(f"{i}. {name}: {memory/1024/1024:.2f} MB")
```

运行脚本以查看比较结果：

```bash
python3 /home/labex/project/compare_structures.py
```

输出将显示每种数据结构的内存使用情况，以及从内存效率最高到最低的排名。

## 理解不同的数据结构

1. **元组（Tuples）**：

   - 元组是轻量级且不可变的序列。这意味着一旦创建了元组，就不能更改其元素。
   - 你可以通过数字索引访问元组中的元素，例如 `record[0]`、`record[1]` 等。
   - 它们的内存效率非常高，因为结构简单。
   - 然而，它们的可读性较差，因为你需要记住每个元素的索引。

2. **字典（Dictionaries）**：

   - 字典使用键值对，这允许你通过名称访问元素。
   - 它们的可读性更强，例如，你可以使用 `record['route']`、`record['date']` 等。
   - 由于用于存储键值对的哈希表开销，它们的内存使用量较高。
   - 它们很灵活，因为你可以轻松地添加或删除字段。

3. **命名元组（Named Tuples）**：

   - 命名元组结合了元组的效率和按名称访问元素的能力。
   - 你可以使用点号表示法访问元素，例如 `record.route`、`record.date` 等。
   - 它们和普通元组一样是不可变的。
   - 它们的内存效率比字典高。

4. **普通类（Regular Classes）**：

   - 普通类遵循面向对象的方法，具有命名属性。
   - 你可以使用点号表示法访问属性，例如 `record.route`、`record.date` 等。
   - 你可以为普通类添加方法来定义行为。
   - 它们使用更多的内存，因为每个实例都有一个实例字典来存储其属性。

5. **使用 `__slots__` 的类（Classes with `__slots__`）**：
   - 使用 `__slots__` 的类是经过内存优化的类。它们避免使用实例字典，从而节省内存。
   - 它们仍然提供对属性的命名访问，例如 `record.route`、`record.date` 等。
   - 它们限制在对象创建后添加新属性。
   - 它们的内存效率比普通类高。

## 何时使用每种方法

- **元组（Tuples）**：当内存是关键因素，并且你只需要对数据进行简单的索引访问时，使用元组。
- **字典（Dictionaries）**：当你需要灵活性，例如数据中的字段可能会变化时，使用字典。
- **命名元组（Named Tuples）**：当你需要可读性和内存效率时，使用命名元组。
- **普通类（Regular Classes）**：当你需要为数据添加行为（方法）时，使用普通类。
- **使用 `__slots__` 的类（Classes with `__slots__`）**：当你需要行为和最大内存效率时，使用使用 `__slots__` 的类。

通过为你的需求选择合适的数据结构，你可以显著提高 Python 程序的性能和内存使用效率，尤其是在处理大型数据集时。
