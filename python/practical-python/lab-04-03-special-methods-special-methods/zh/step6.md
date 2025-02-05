# 绑定方法

尚未通过函数调用运算符 `()` 调用的方法称为 _绑定方法_。它作用于其所属的实例。

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

绑定方法常常是粗心导致的不易察觉的错误来源。例如：

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

或者是难以调试的隐蔽行为。

```python
f = open(filename, 'w')
...
f.close     # 哎呀，什么都没做。`f` 仍然是打开的状态。
```

在这两种情况下，错误都是由于忘记加上尾随的括号导致的。例如，`s.cost()` 或 `f.close()`。
