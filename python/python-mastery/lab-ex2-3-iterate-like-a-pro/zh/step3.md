# 生成器表达式与内存效率

在这一步中，我们将探索生成器表达式。当你在 Python 中处理大型数据集时，它们非常有用。它们可以让你的代码在内存使用上更加高效，这在处理大量数据时至关重要。

## 理解生成器表达式

生成器表达式与列表推导式类似，但有一个关键区别。当你使用列表推导式时，Python 会一次性创建一个包含所有结果的列表。这可能会占用大量内存，特别是在处理大型数据集时。而生成器表达式会根据需要逐个生成结果。这意味着它不需要一次性将所有结果存储在内存中，从而可以节省大量内存。

让我们看一个简单的例子，了解它是如何工作的：

```python
# Start a new Python session if needed
# python3

# List comprehension (creates a list in memory)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Generator expression (creates a generator object)
squares_gen = (x*x for x in nums)
print(squares_gen)  # This doesn't print the values, just the generator object

# Iterate through the generator to get values
for n in squares_gen:
    print(n)
```

当你运行这段代码时，你会看到以下输出：

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

关于生成器，有一点需要注意：它们只能被迭代一次。一旦你遍历完生成器中的所有值，它就会耗尽，你无法再次获取这些值。

```python
# Try to iterate again over the same generator
for n in squares_gen:
    print(n)  # Nothing will be printed, as the generator is already exhausted
```

你还可以使用 `next()` 函数手动逐个从生成器中获取值。

```python
# Create a fresh generator
squares_gen = (x*x for x in nums)

# Get values one by one
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

当生成器中没有更多值时，调用 `next()` 会引发 `StopIteration` 异常。

## 使用 `yield` 的生成器函数

对于更复杂的生成器逻辑，你可以使用 `yield` 语句编写生成器函数。生成器函数是一种特殊类型的函数，它使用 `yield` 逐个返回值，而不是一次性返回单个结果。

```python
def squares(nums):
    for x in nums:
        yield x*x

# Use the generator function
for n in squares(nums):
    print(n)
```

当你运行这段代码时，你会看到以下输出：

```
1
4
9
16
25
```

## 使用生成器表达式减少内存使用

现在，让我们看看在处理大型数据集时，生成器表达式如何节省内存。我们将使用 CTA 公交数据文件，它相当大。

首先，让我们尝试一种内存密集型的方法：

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

现在，退出 Python 并重新启动，以便与基于生成器的方法进行比较：

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Use generator expressions for all operations
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

你应该会注意到这两种方法在内存使用上有显著差异。基于生成器的方法会逐步处理数据，而不是一次性将所有数据加载到内存中，这样在内存使用上更加高效。

## 结合归约函数使用生成器表达式

当生成器表达式与 `sum()`、`min()`、`max()`、`any()` 和 `all()` 等处理整个序列并产生单个结果的函数结合使用时，特别有用。

让我们看一些例子：

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calculate the total value of the portfolio
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Total portfolio value: {total_value}")

# Find the minimum number of shares in any holding
min_shares = min(s['shares'] for s in portfolio)
print(f"Minimum shares in any holding: {min_shares}")

# Check if any stock is IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Portfolio contains IBM: {has_ibm}")

# Check if all stocks are IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"All stocks are IBM: {all_ibm}")

# Count IBM shares
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Total IBM shares: {ibm_shares}")
```

生成器表达式在字符串操作中也很有用。以下是如何连接元组中的值：

```python
s = ('GOOG', 100, 490.10)
# This would fail: ','.join(s)
# Use a generator expression to convert all items to strings
joined = ','.join(str(x) for x in s)
print(joined)  # Output: 'GOOG,100,490.1'
```

在这些例子中，使用生成器表达式的关键优势在于不会创建中间列表，从而使代码在内存使用上更加高效。
