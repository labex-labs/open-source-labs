# 处理 Python 列表

列表是 Python 中的一种数据结构。数据结构是一种组织和存储数据的方式，以便能够高效地使用数据。列表非常通用，因为它们可以存储不同类型的项，如数字、字符串，甚至其他列表。在这一步中，我们将学习如何对列表执行各种操作。

## 从字符串创建列表

要开始处理 Python 列表，你首先需要打开一个 Python 交互式会话。这就像是一个特殊的环境，你可以立即在其中编写和运行 Python 代码。要启动这个会话，请在终端中输入以下命令：

```bash
python3
```

进入 Python 交互式会话后，我们将从一个字符串创建一个列表。字符串只是一个字符序列。我们将定义一个包含一些用空格分隔的股票代码的字符串。然后，我们将把这个字符串转换为一个列表。每个股票代码将成为列表中的一个元素。

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # 按空白字符分割字符串
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

`split()` 方法用于在有空白字符的地方将字符串拆分成多个部分。每个部分随后成为新列表中的一个元素。

## 访问和修改列表元素

和字符串一样，列表也支持索引。索引意味着我们可以通过元素的位置来访问列表中的单个元素。在 Python 中，列表中的第一个元素的索引为 0，第二个元素的索引为 1，依此类推。我们还可以使用负索引从列表末尾访问元素。最后一个元素的索引为 -1，倒数第二个元素的索引为 -2，依此类推。

与字符串不同的是，列表元素可以被修改。这意味着我们可以更改列表中某个元素的值。

```python
>>> symlist[0]    # 第一个元素
'HPQ'
>>> symlist[1]    # 第二个元素
'AAPL'
>>> symlist[-1]   # 最后一个元素
'GOOG'
>>> symlist[-2]   # 倒数第二个元素
'YHOO'

>>> symlist[2] = 'AIG'    # 替换第三个元素
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## 遍历列表

通常，我们需要对列表中的每个元素执行相同的操作。我们可以使用 `for` 循环来实现这一点。`for` 循环允许我们逐个遍历列表中的每个元素，并对其执行特定的操作。

```python
>>> for s in symlist:
...     print('s =', s)
...
```

运行这段代码时，你会看到列表中的每个元素都带有 `s =` 标签被打印出来。

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## 检查成员资格

有时，我们需要检查某个特定的项是否存在于列表中。我们可以使用 `in` 运算符来完成这个任务。如果该项在列表中，`in` 运算符返回 `True`；如果不在，则返回 `False`。

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## 添加和删除元素

列表有内置的方法，允许我们添加和删除元素。`append()` 方法将一个元素添加到列表的末尾。`insert()` 方法在列表的特定位置插入一个元素。`remove()` 方法根据元素的值从列表中删除该元素。

```python
>>> symlist.append('RHT')    # 在末尾添加一个元素
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # 在特定位置插入元素
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # 根据值删除元素
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

如果你尝试删除列表中不存在的元素，Python 会引发错误。

```python
>>> symlist.remove('MSFT')
```

你会看到类似这样的错误消息：

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

我们还可以使用 `index()` 方法找到元素在列表中的位置。

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # 验证该位置的元素
'YHOO'
```

## 排序列表

列表可以进行原地排序，这意味着原始列表会被修改。我们可以按字母顺序或逆序对列表进行排序。

```python
>>> symlist.sort()    # 按字母顺序排序
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # 逆序排序
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## 嵌套列表

列表可以包含任何类型的对象，包括其他列表。这被称为嵌套列表。

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

要访问嵌套列表中的元素，我们使用多个索引。第一个索引选择外部列表元素，第二个索引选择内部列表元素。

```python
>>> items[0]    # 第一个元素（即 symlist）
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # symlist 中的第二个元素
'RHT'
>>> items[0][1][2]    # 'RHT' 中的第三个字符
'T'
>>> items[1]    # 第二个元素（即 nums 列表）
[101, 102, 103]
>>> items[1][1]    # nums 中的第二个元素
102
```

当你完成 Python 交互式会话的操作后，可以通过输入以下内容退出：

```python
>>> exit()
```
