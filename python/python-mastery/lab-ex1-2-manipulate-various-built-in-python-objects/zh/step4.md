# 处理 Python 字典

在 Python 中，字典是一种基础的数据结构。它们是键值对存储，这意味着你可以将一个值（值）映射到另一个值（键）。在处理具有自然键值关系的数据时，这非常有用。例如，你可能想将一个人的名字（键）映射到他们的年龄（值），或者就像我们在这个实验中看到的，将股票代码（键）映射到它们的价格（值）。

## 创建和访问字典

让我们从打开一个新的 Python 交互式会话开始。这就像进入一个特殊的环境，你可以逐行编写和运行 Python 代码。要启动这个会话，打开你的终端并输入以下命令：

```bash
python3
```

进入 Python 交互式会话后，你可以创建一个字典。在我们的例子中，我们将创建一个将股票代码映射到其价格的字典。以下是创建方法：

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

在第一行，我们创建了一个名为 `prices` 的字典，并为其分配了一些键值对。键是股票代码（`IBM`、`GOOG`、`AAPL`），值是相应的价格。第二行只是显示了 `prices` 字典的内容。

现在，让我们看看如何使用键来访问和修改字典中的值。

```python
>>> prices['IBM']    # 访问键 'IBM' 对应的值
91.1

>>> prices['IBM'] = 123.45    # 更新现有值
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # 添加一个新的键值对
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

在第一行，我们访问与键 `IBM` 关联的值。在第二行和第三行，我们更新了键 `IBM` 对应的值，然后添加了一个新的键值对（`HPQ`，价格为 `26.15`）。

## 获取字典的键

有时，你可能想获取字典中所有键的列表。有几种方法可以做到这一点。

```python
>>> list(prices)    # 将字典的键转换为列表
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

在这里，我们使用 `list()` 函数将 `prices` 字典的键转换为一个列表。

你还可以使用 `keys()` 方法，它会返回一个名为 `dict_keys` 的特殊对象。

```python
>>> prices.keys()    # 返回一个 dict_keys 对象
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## 获取字典的值

同样，你可能想获取字典中的所有值。你可以使用 `values()` 方法来实现。

```python
>>> prices.values()    # 返回一个 dict_values 对象
dict_values([123.45, 490.1, 312.23, 26.15])
```

这个方法返回一个 `dict_values` 对象，其中包含 `prices` 字典中的所有值。

## 删除项

如果你想从字典中删除一个键值对，可以使用 `del` 关键字。

```python
>>> del prices['AAPL']    # 删除 'AAPL' 条目
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

在这里，我们从 `prices` 字典中删除了键为 `AAPL` 的键值对。

## 检查键是否存在

要检查一个键是否存在于字典中，可以使用 `in` 运算符。

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

如果键存在于字典中，`in` 运算符返回 `True`，否则返回 `False`。

## 字典方法

字典有几个有用的方法。让我们来看看其中的几个。

```python
>>> prices.get('MSFT', 0)    # 获取值，如果键不存在则返回默认值
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # 一次性更新多个值
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

`get()` 方法尝试获取与键关联的值。如果键不存在，它返回一个默认值（在这种情况下是 `0`）。`update()` 方法用于一次性更新字典中的多个键值对。

当你完成 Python 交互式会话的操作后，可以通过输入以下内容退出：

```python
>>> exit()
```
