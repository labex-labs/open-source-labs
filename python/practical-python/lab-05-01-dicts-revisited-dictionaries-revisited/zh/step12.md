# 方法解析顺序（Method Resolution Order，MRO）

Python 会预先计算出一个继承链，并将其存储在类的 _MRO_ 属性中。你可以查看它。

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

这个链被称为**方法解析顺序**。为了查找一个属性，Python 会按顺序遍历 MRO。第一个匹配项即为结果。
