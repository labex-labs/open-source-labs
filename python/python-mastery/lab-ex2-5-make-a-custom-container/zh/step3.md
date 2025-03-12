# 使用列向数据优化内存

在传统的数据存储中，我们通常将每条记录存储为一个单独的字典，这种方法称为行向（row-oriented）存储。然而，这种方法会消耗大量的内存。另一种方法是按列存储数据。在列向（column-oriented）存储方法中，我们为每个属性创建单独的列表，每个列表保存该特定属性的所有值。这有助于我们节省内存。

1. 首先，你需要在项目目录中创建一个新的 Python 文件。这个文件将包含以列向方式读取数据的代码。将文件命名为 `readrides.py`。你可以在终端中使用以下命令来完成此操作：

```bash
cd ~/project
touch readrides.py
```

`cd ~/project` 命令将当前目录更改为你的项目目录，`touch readrides.py` 命令创建一个名为 `readrides.py` 的新空文件。

2. 接下来，在 WebIDE 编辑器中打开 `readrides.py` 文件。然后，将以下 Python 代码添加到文件中。这段代码定义了一个名为 `read_rides_as_columns` 的函数，该函数从 CSV 文件中读取公交乘车数据，并将其存储在四个单独的列表中，每个列表代表一列数据。

```python
# readrides.py
import csv
import sys
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

在这段代码中，我们首先导入了必要的模块 `csv`、`sys` 和 `tracemalloc`。`csv` 模块用于读取 CSV 文件，`sys` 可用于与系统相关的操作（尽管在这个函数中未使用），`tracemalloc` 用于内存分析。在函数内部，我们初始化了四个空列表来存储不同列的数据。然后，我们打开文件，跳过标题行，并遍历文件中的每一行，将相应的值追加到适当的列表中。最后，我们返回一个包含这四个列表的字典。

3. 现在，让我们分析一下为什么列向存储方法可以节省内存。我们将在 Python shell 中进行分析。运行以下代码：

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

在这段代码中，我们首先导入了刚刚创建的 `readrides` 模块和 `tracemalloc` 模块。然后，我们估算了行向存储方法的内存使用量。我们假设每个字典的开销约为 240 字节，并将其乘以原始文件中的行数，以得到行向数据的总内存使用量。对于列向存储方法，我们假设在 64 位系统上，每个指针占用 8 字节。由于我们有 4 列，且每个条目有一个指针，因此我们计算出列向数据的总内存使用量。最后，我们通过从行向存储的内存使用量中减去列向存储的内存使用量来计算内存节省量。

这个计算表明，与使用字典的行向存储方法相比，列向存储方法应该可以节省约 120MB 的内存。

4. 让我们使用 `tracemalloc` 模块测量实际的内存使用量来验证这一点。运行以下代码：

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

在这段代码中，我们首先使用 `tracemalloc.start()` 开始跟踪内存。然后，我们调用 `read_rides_as_columns` 函数从 `ctabus.csv` 文件中读取数据。之后，我们使用 `tracemalloc.get_traced_memory()` 获取当前和峰值内存使用量。最后，我们使用 `tracemalloc.stop()` 停止跟踪内存。

输出将显示你列向数据结构的实际内存使用量。这应该明显低于我们对行向存储方法的理论估算值。

显著的内存节省来自于消除了数千个字典对象的开销。Python 中的每个字典都有固定的开销，无论它包含多少项。通过使用列向存储，我们只需要几个列表，而不是数千个字典。
