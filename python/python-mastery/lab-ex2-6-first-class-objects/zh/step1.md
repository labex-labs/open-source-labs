# 理解 Python 中的一等对象

在 Python 中，一切都被视为对象，这包括函数和类型。这意味着什么呢？这意味着你可以将函数和类型存储在数据结构中，将它们作为参数传递给其他函数，甚至从其他函数中返回它们。这是一个非常强大的概念，我们将以 CSV 数据处理为例来探索它。

## 探索一等类型

首先，让我们启动 Python 解释器。在 WebIDE 中打开一个新的终端，然后输入以下命令。这个命令将启动 Python 解释器，我们将在其中运行 Python 代码。

```bash
python3
```

在 Python 中处理 CSV 文件时，我们经常需要将从这些文件中读取的字符串转换为合适的数据类型。例如，CSV 文件中的数字可能会被读取为字符串，但我们希望在 Python 代码中把它作为整数或浮点数使用。为此，我们可以创建一个转换函数列表。

```python
coltypes = [str, int, float]
```

注意，我们创建的列表中包含的是实际的类型函数，而不是字符串。在 Python 中，类型是一等对象，这意味着我们可以像对待其他任何对象一样对待它们。我们可以将它们放入列表中、传递它们，并在代码中使用它们。

现在，让我们从一个投资组合（portfolio）的 CSV 文件中读取一些数据，看看如何使用这些转换函数。

```python
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
```

当你运行这段代码时，你应该会看到类似于以下的输出。这是 CSV 文件中的第一行数据，以字符串列表的形式表示。

```
['AA', '100', '32.20']
```

接下来，我们将使用 `zip` 函数。`zip` 函数接受多个可迭代对象（如列表或元组），并将它们的元素配对。我们将使用它把行中的每个值与其对应的类型转换函数配对。

```python
r = list(zip(coltypes, row))
print(r)
```

这将产生以下输出。每一对都包含一个类型函数和 CSV 文件中的一个字符串值。

```
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

现在我们有了这些配对，就可以应用每个函数将值转换为合适的类型。

```python
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
```

输出将显示这些值已被转换为合适的类型。字符串 'AA' 仍然是字符串，'100' 变成了整数 100，'32.20' 变成了浮点数 32.2。

```
['AA', 100, 32.2]
```

我们还可以将这些值与它们的列名组合起来，创建一个字典。字典是 Python 中一种有用的数据结构，它允许我们存储键值对。

```python
record_dict = dict(zip(headers, record))
print(record_dict)
```

输出将是一个字典，其中键是列名，值是转换后的数据。

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

你可以使用单个推导式（comprehension）完成所有这些步骤。推导式是在 Python 中创建列表、字典或集合的简洁方式。

```python
result = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(result)
```

输出将与之前的字典相同。

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

当你在 Python 解释器中完成工作后，可以通过输入以下命令退出。

```python
exit()
```

这个演示展示了 Python 将函数视为一等对象如何实现强大的数据处理技术。通过能够将类型和函数视为对象，我们可以编写更灵活、更简洁的代码。
