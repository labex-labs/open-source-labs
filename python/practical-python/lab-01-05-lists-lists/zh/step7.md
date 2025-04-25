# 练习 1.19：提取和重新赋值列表元素

尝试进行一些查找操作：

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

尝试重新赋值一个值：

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

进行一些切片操作：

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

创建一个空列表并向其中追加一个元素。

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

你可以将列表的一部分重新赋值为另一个列表。例如：

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

当你这样做时，左侧的列表（`symlist`）会根据需要进行调整大小，以使右侧的列表（`mysyms`）能够适配。例如，在上述示例中，`symlist` 的最后两个元素被 `mysyms` 中的单个元素替换。
