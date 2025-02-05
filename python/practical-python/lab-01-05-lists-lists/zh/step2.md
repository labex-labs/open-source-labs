# 列表操作

列表可以容纳任何类型的元素。使用 `append()` 方法添加新元素：

```python
names.append('Murphy')    # 在末尾添加
names.insert(2, 'Aretha') # 在中间插入
```

使用 `+` 来连接列表：

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

列表通过整数进行索引，从 0 开始。

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

负索引从末尾开始计数。

```python
names[-1] # 'Curtis'
```

你可以更改列表中的任何元素。

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

获取列表的长度。

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

成员测试 (`in`, `not in`)。

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

复制 (`s * n`)。

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
