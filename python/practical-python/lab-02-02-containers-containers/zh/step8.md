# 集合

集合是无序的唯一元素的集合。

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# 另一种语法
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

集合对于成员测试很有用。

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

集合对于消除重复项也很有用。

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

其他集合操作：

```python
unique.add('CAT')        # 添加一个元素
unique.remove('YHOO')    # 移除一个元素

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # 集合并集 { 'a', 'b', 'c', 'd' }
s1 & s2                 # 集合交集 { 'c' }
s1 - s2                 # 集合差集 { 'a', 'b' }
```

在这些练习中，你将开始构建本课程剩余部分使用的一个主要程序。在 `report.py` 文件中完成你的工作。
