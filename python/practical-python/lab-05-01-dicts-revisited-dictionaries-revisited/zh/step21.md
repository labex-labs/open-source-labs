# 练习 5.4：绑定方法

Python 一个微妙的特性是，调用方法实际上涉及两个步骤，以及所谓的绑定方法。例如：

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

绑定方法实际上包含了调用方法所需的所有部分。例如，它们会记录实现该方法的函数：

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

这与 `Stock` 字典中的值相同。

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

绑定方法还会记录实例，即 `self` 参数。

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

当你使用 `()` 调用函数时，所有部分就会组合在一起。例如，调用 `s(25)` 实际上是这样做的：

```python
>>> s.__func__(s.__self__, 25)    # 与 s(25) 相同
>>> goog.shares
50
>>>
```
