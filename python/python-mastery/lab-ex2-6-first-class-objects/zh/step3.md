# 探索 Python 的内存模型

Python 的内存模型在决定对象如何存储在内存中以及如何被引用方面起着至关重要的作用。理解这个模型非常重要，尤其是在处理大型数据集时，因为它会显著影响 Python 程序的性能和内存使用情况。在这一步中，我们将特别关注 Python 如何处理字符串对象，并探索优化大型数据集内存使用的方法。

## 数据集中的字符串重复问题

芝加哥交通管理局（CTA）的公交数据包含许多重复的值，例如公交线路名称。如果处理不当，数据集中的重复值可能会导致内存使用效率低下。为了了解这个问题的严重程度，让我们首先检查数据集中有多少个唯一的公交线路字符串。

首先，打开 Python 解释器。你可以在终端中运行以下命令来实现：

```bash
python3
```

Python 解释器打开后，我们将加载 CTA 公交数据并找出唯一的公交线路。以下是实现此功能的代码：

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

在这段代码中，我们首先导入 `reader` 模块，该模块可能包含一个将 CSV 文件读取为字典的函数。然后，我们使用 `read_csv_as_dicts` 函数从 `ctabus.csv` 文件中加载数据。第二个参数 `[str, str, str, int]` 指定了 CSV 文件中每列的数据类型。之后，我们使用集合推导式找出数据集中所有唯一的公交线路名称，并打印出唯一公交线路名称的数量。

输出应该是：

```
Number of unique route names: 181
```

现在，让我们检查为这些公交线路创建了多少个不同的字符串对象。尽管只有 181 个唯一的公交线路名称，但 Python 可能会为数据集中每次出现的公交线路名称创建一个新的字符串对象。为了验证这一点，我们将使用 `id()` 函数获取每个字符串对象的唯一标识符。

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

输出可能会让你感到惊讶：

```
Number of unique route string objects: 542305
```

这表明只有 181 个唯一的公交线路名称，但有超过 500,000 个唯一的字符串对象。这是因为即使值相同，Python 也会为每一行创建一个新的字符串对象。这可能会导致大量的内存浪费，尤其是在处理大型数据集时。

## 使用字符串驻留（String Interning）节省内存

Python 提供了一种使用 `sys.intern()` 函数来“驻留”（复用）字符串的方法。当数据集中有许多重复的字符串时，字符串驻留可以节省内存。当你对一个字符串进行驻留操作时，Python 会检查 intern 池（字符串驻留池）中是否已经存在相同的字符串。如果存在，它将返回对现有字符串对象的引用，而不是创建一个新的对象。

让我们通过一个简单的例子来演示字符串驻留的工作原理：

```python
import sys

# Without interning
a = 'hello world'
b = 'hello world'
print(f"a is b (without interning): {a is b}")

# With interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a is b (with interning): {a is b}")
```

在这段代码中，我们首先创建了两个具有相同值的字符串变量 `a` 和 `b`，但没有进行驻留操作。`is` 运算符用于检查两个变量是否引用同一个对象。在没有驻留的情况下，`a` 和 `b` 是不同的对象，因此 `a is b` 返回 `False`。然后，我们使用 `sys.intern()` 对两个字符串进行驻留操作。驻留后，`a` 和 `b` 引用 intern 池中的同一个对象，因此 `a is b` 返回 `True`。

输出应该是：

```
a is b (without interning): False
a is b (with interning): True
```

现在，让我们在读取 CTA 公交数据时使用字符串驻留来减少内存使用。我们还将使用 `tracemalloc` 模块来跟踪驻留前后的内存使用情况。

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for the route column
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Check unique route objects again
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects (with interning): {len(routeids)}")

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

在这段代码中，我们首先使用 `tracemalloc.start()` 开始内存跟踪。然后，我们通过将 `sys.intern` 作为第一列的数据类型，对公交线路列进行驻留操作来读取 CTA 公交数据。之后，我们再次检查唯一的公交线路字符串对象的数量，并打印当前和峰值内存使用情况。

输出应该类似于：

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

让我们重启解释器，尝试对公交线路和日期字符串都进行驻留操作，看看是否可以进一步减少内存使用。

```python
exit()
```

再次启动 Python：

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for both route and date columns
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (interning route and date): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (interning route and date): {peak / 1024 / 1024:.2f} MB")
```

输出应该显示内存使用进一步减少：

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

这展示了理解 Python 的内存模型并使用字符串驻留等技术如何帮助优化程序，尤其是在处理包含重复值的大型数据集时。

最后，退出 Python 解释器：

```python
exit()
```
