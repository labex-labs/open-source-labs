# 创建新列表

列表推导式通过对序列中的每个元素应用一个操作来创建一个新列表。

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

另一个示例：

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

一般语法为：`[ <表达式> for <变量名> in <序列> ]`。
