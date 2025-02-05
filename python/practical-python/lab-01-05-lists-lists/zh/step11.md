# 练习1.23：排序

想对列表进行排序吗？使用 `sort()` 方法。试试看：

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

想按降序排序吗？试试这个：

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

注意：对列表进行排序会“就地”修改其内容。也就是说，列表中的元素会被重新排列，但不会因此创建新的列表。
