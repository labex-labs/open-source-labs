# 第1部分：数字

在Python中，数值计算的方式正如你所期望的那样。例如：

```python
>>> 3 + 4*5
23
>>> 23.45 / 1e-02
2345.0
>>>
```

请注意，Python 2和Python 3中的整数除法有所不同。

```python
>>> 7 / 4      # 在Python 2中，这会截断为1
1.75
>>> 7 // 4     # 截断除法
1
>>>
```

如果你想在Python 2中使用Python 3的行为，可以这样做：

```python
>>> from __future__ import division
>>> 7 / 4
1.75
>>> 7 // 4      # 截断除法
1
>>>
```

数字有一小组方法，其中许多实际上是相当新的，甚至有经验的Python程序员也会忽略它们。试试其中一些方法。

```python
>>> x = 1172.5
>>> x.as_integer_ratio()
(2345, 2)
>>> x.is_integer()
False
>>> y = 12345
>>> y.numerator
12345
>>> y.denominator
1
>>> y.bit_length()
14
>>>
```
