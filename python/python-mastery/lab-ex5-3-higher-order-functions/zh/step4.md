# 使用 `map()` 函数

在 Python 中，高阶函数是可以接受另一个函数作为参数或返回一个函数作为结果的函数。Python 的 `map()` 函数就是高阶函数的一个很好的例子。它是一个强大的工具，允许你将给定的函数应用于可迭代对象（如列表或元组）中的每个元素。将函数应用于每个元素后，它会返回一个包含结果的迭代器。这个特性使 `map()` 非常适合处理数据序列，比如 CSV 文件中的行。

`map()` 函数的基本语法如下：

```python
map(function, iterable, ...)
```

这里，`function` 是你想要对 `iterable` 中的每个元素执行的操作。`iterable` 是一个元素序列，如列表或元组。

让我们看一个简单的例子。假设你有一个数字列表，你想对列表中的每个数字进行平方运算。你可以使用 `map()` 函数来实现这一点。以下是具体做法：

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

在这个例子中，我们首先定义了一个名为 `numbers` 的列表。然后，我们使用 `map()` 函数。`lambda` 函数 `lambda x: x * x` 是我们想要对 `numbers` 列表中的每个元素执行的操作。`map()` 函数将这个 `lambda` 函数应用于列表中的每个数字。由于 `map()` 返回一个迭代器，我们使用 `list()` 函数将其转换为列表。最后，我们打印 `squared` 列表，它包含了原始数字的平方值。

现在，让我们看看如何使用 `map()` 函数来修改我们的 `convert_csv()` 函数。之前，我们使用 `for` 循环来遍历 CSV 数据中的行。现在，我们将用 `map()` 函数替换那个 `for` 循环。

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

这个更新后的 `convert_csv()` 函数与之前的版本功能完全相同，但它使用 `map()` 函数代替了 `for` 循环。`map()` 内部的 `lambda` 函数从 CSV 数据中取出每一行，并将 `conversion_func` 应用于该行以及列名。

让我们测试这个更新后的函数，确保它能正常工作。首先，打开终端并导航到项目目录。然后，使用 `reader.py` 文件启动 Python 交互式 shell。

```bash
cd ~/project
python3 -i reader.py
```

进入 Python shell 后，运行以下代码来测试更新后的 `convert_csv()` 函数：

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

运行这段代码后，你应该会看到类似于以下的输出：

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

这个输出表明，使用 `map()` 函数更新后的 `convert_csv()` 函数能正常工作，并且依赖于它的函数也能继续按预期工作。

使用 `map()` 函数有几个优点：

1. 它比 `for` 循环更简洁。你无需为 `for` 循环编写多行代码，使用 `map()` 只需一行代码就能达到相同的效果。
2. 它能清晰地传达你要对序列中的每个元素进行转换的意图。当你看到 `map()` 时，你立刻就知道你正在将一个函数应用于可迭代对象中的每个元素。
3. 它可能更节省内存，因为它返回一个迭代器。迭代器会即时生成值，这意味着它不会一次性将所有结果存储在内存中。在我们的例子中，我们将 `map()` 返回的迭代器转换为了列表，但在某些情况下，你可以直接使用迭代器来节省内存。

要退出 Python shell，你可以输入 `exit()` 或按 Ctrl+D。
