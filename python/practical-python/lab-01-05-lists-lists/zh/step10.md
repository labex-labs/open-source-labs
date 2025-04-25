# 练习 1.22：追加、插入和删除项目

使用 `append()` 方法将符号 `'RHT'` 添加到 `symlist` 的末尾。

```python
>>> symlist.append('RHT') # 追加 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

使用 `insert()` 方法将符号 `'AA'` 作为列表中的第二个项目插入。

```python
>>> symlist.insert(1, 'AA') # 将 'AA' 插入为列表中的第二个项目
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

使用 `remove()` 方法从列表中删除 `'MSFT'`。

```python
>>> symlist.remove('MSFT') # 删除 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

在列表末尾追加 `'YHOO'` 的重复项。

**注意：列表中有重复值是完全可以的。**

```python
>>> symlist.append('YHOO') # 追加 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

使用 `index()` 方法找到列表中 `'YHOO'` 的第一个位置。

```python
>>> symlist.index('YHOO') # 找到 'YHOO' 的第一个索引
4
>>> symlist[4]
'YHOO'
>>>
```

计算 `'YHOO'` 在列表中出现的次数：

```python
>>> symlist.count('YHOO')
2
>>>
```

删除 `'YHOO'` 的第一次出现。

```python
>>> symlist.remove('YHOO') # 删除第一次出现的 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

需要说明的是，没有方法可以找到或删除一个项目的所有出现。不过，我们将在第 2 节中看到一种优雅的方法来做到这一点。
