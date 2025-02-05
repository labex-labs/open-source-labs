# zip() 函数

`zip` 函数接受多个序列，并创建一个将它们组合在一起的迭代器。

```python
columns = ['name','shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name', 'GOOG'), ('shares', 100), ('price', 490.1)
```

要获得结果，你必须进行迭代。如前所示，你可以使用多个变量来解包元组。

```python
for column, value in pairs:
  ...
```

`zip` 的一个常见用途是创建用于构建字典的键/值对。

```python
d = dict(zip(columns, values))
```
