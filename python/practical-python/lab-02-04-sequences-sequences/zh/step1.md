# 序列数据类型

Python 有三种**序列**数据类型。

- 字符串：`'Hello'`。字符串是字符序列。
- 列表：`[1, 4, 5]`。
- 元组：`('GOOG', 100, 490.1)`。

所有序列都是有序的，由整数索引，并且有一个长度。

```python
a = 'Hello'               # 字符串
b = [1, 4, 5]             # 列表
c = ('GOOG', 100, 490.1)  # 元组

# 索引顺序
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# 序列长度
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

序列可以复制：`s * n`。

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

相同类型的序列可以连接：`s + t`。

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```
