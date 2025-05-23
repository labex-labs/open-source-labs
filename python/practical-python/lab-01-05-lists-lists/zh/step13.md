# 练习 1.25：包含任何内容的列表

列表可以包含任何类型的对象，包括其他列表（例如，嵌套列表）。试试看：

```python
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

仔细观察上面的输出。`items` 是一个包含三个元素的列表。第一个元素是一个字符串，但其他两个元素是列表。

你可以通过使用多个索引操作来访问嵌套列表中的元素。

```python
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
```

尽管从技术上讲可以创建非常复杂的列表结构，但一般来说，你要保持简单。通常列表包含的元素都是同一种类型的值。例如，一个完全由数字组成的列表或一个文本字符串列表。在同一个列表中混合不同类型的数据通常会让你头疼不已，所以最好避免这样做。
