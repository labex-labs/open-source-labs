# 探索 collections 模块

在 Python 中，像列表、字典和集合这样的内置容器非常有用。然而，Python 的 `collections` 模块更进一步，提供了专门的容器数据类型，扩展了这些内置容器的功能。让我们仔细看看其中一些有用的数据类型。

你将继续在 Python 终端中操作，并按照下面的示例进行学习。

## Counter

`Counter` 类是字典的一个子类。它的主要用途是对可哈希对象进行计数。它提供了一种便捷的方式来统计元素数量，并支持多种操作。

首先，我们需要导入 `Counter` 类和一个读取投资组合的函数。然后，我们将从 CSV 文件中读取一个投资组合。

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

现在，我们将创建一个 `Counter` 对象，按股票名称统计每只股票的股数。

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

`Counter` 对象的一个很棒的特性是，它会自动将新键的计数初始化为 0。这意味着在增加计数之前，你不必检查键是否存在，这简化了累加计数的代码。

计数器还带有特殊的方法。例如，`most_common()` 方法在数据分析中非常有用。

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

此外，计数器可以使用算术运算进行组合。

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict

`defaultdict` 与普通字典类似，但它有一个独特的特性。它为尚未存在的键提供默认值。这可以简化你的代码，因为在使用键之前，你不再需要检查键是否存在。

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

当你创建 `defaultdict(list)` 时，它会自动为每个新键创建一个新的空列表。因此，即使键之前不存在，你也可以直接向键的值中追加元素。这消除了检查键是否存在并手动创建空列表的需要。

你还可以使用其他默认工厂函数。例如，你可以使用 `int`、`float` 甚至你自己的自定义函数。

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

`collections` 模块中的这些专门容器类型在处理数据时可以使你的代码更加简洁和高效。
