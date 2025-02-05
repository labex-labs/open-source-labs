# 协调类型

在当前的 `Stock` 类中，有一个 `_types` 类变量，它在从文件读取时提供转换功能，但也有一些特性在强制规定类型。到底谁说了算呢？修改特性定义，使其使用 `_types` 类变量中指定的类型。确保当通过子类化更改类型时，这些特性仍然有效。例如：

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        _types = (str, int, Decimal)

>>> s = DStock('AA', 50, Decimal('91.1'))
>>> s.price = 92.3
Traceback (最近一次调用最后):
...
TypeError: 期望一个 Decimal
>>>
```

**讨论**

在这个实验结束时得到的 `Stock` 类是一个由特性、类型检查、构造函数和其他细节组成的混乱局面。想象一下，维护包含数十个或数百个此类类定义的代码会有多麻烦。

我们将弄清楚如何大幅简化这些事情，但这需要一些时间和一些更高级的技术。请继续关注。
