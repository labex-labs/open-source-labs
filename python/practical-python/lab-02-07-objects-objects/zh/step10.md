# 一切皆对象

数字、字符串、列表、函数、异常、类、实例等都是对象。这意味着所有可以被命名的对象都能作为数据传递、放入容器等，没有任何限制。不存在 _特殊_ 类型的对象。有时人们会说所有对象都是“一等公民（first-class）”。

一个简单的例子：

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module 'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

在这里，`items` 是一个包含函数、模块和异常的列表。你可以直接使用列表中的元素来替代原来的名称：

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

能力越大，责任越大。仅仅因为你能这么做，并不意味着你就应该这么做。

在这组练习中，我们将探讨一等公民对象所带来的一些强大功能。
