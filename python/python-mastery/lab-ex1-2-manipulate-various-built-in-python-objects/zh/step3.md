# 第3部分：列表操作

在第一部分中，你处理了包含股票代码的字符串。例如：

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```

定义上述变量，并使用字符串的 `split()` 操作将其拆分为名称列表：

```python
>>> symlist = symbols.split()
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## 提取和重新分配列表元素

列表的工作方式类似于数组，你可以通过数字索引查找和修改元素。尝试一些查找操作：

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'YHOO'
>>>
```

尝试重新分配其中一个元素：

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## 遍历列表项

`for` 循环通过遍历序列（如列表）中的数据来工作。通过输入以下循环并观察发生的情况来检查这一点：

```python
>>> for s in symlist:
        print('s =', s)

... 查看输出...
```

## 成员测试

使用 `in` 运算符检查 `'AIG'`、`'AA'` 和 `'CAT'` 是否在符号列表中。

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>>
```

## 添加、插入和删除项

使用 `append()` 方法将符号 `'RHT'` 添加到 `symlist` 的末尾。

```python
>>> symlist.append('RHT')
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

使用 `insert()` 方法将符号 `'AA'` 插入到列表的第二个位置。

```python
>>> symlist.insert(1,'AA')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

使用 `remove()` 方法从列表中删除 `'MSFT'`。

```python
>>> symlist.remove('MSFT')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

再次调用 `remove()`，看看如果找不到该项会发生什么。

```python
>>> symlist.remove('MSFT')
... 观察发生的情况...
>>>
```

使用 `index()` 方法找到 `'YHOO'` 在列表中的位置。

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]
'YHOO'
>>>
```

## 列表排序

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

注意：对列表进行排序会“就地”修改其内容。也就是说，列表的元素会被重新排列，但不会因此创建新的列表。

## 包含任何内容的列表

列表可以包含任何类型的对象，包括其他列表（例如，嵌套列表）。试试看：

```python
>>> nums = [101,102,103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

仔细观察上述输出。`items` 是一个包含两个元素的列表。每个元素都是一个列表。

尝试一些嵌套列表查找操作：

```python
>>> items[0]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]
'RHT'
>>> items[0][1][2]
'T'
>>> items[1]
[101, 102, 103]
>>> items[1][1]
102
>>>
```
