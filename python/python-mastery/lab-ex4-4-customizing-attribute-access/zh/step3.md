# 委托：继承的替代方案

委托有时被用作继承的替代方案。其思路与你在（b）部分定义的代理类几乎相同。尝试定义以下类：

```python
>>> class Spam:
        def a(self):
            print('Spam.a')
        def b(self):
            print('Spam.b')

>>>
```

现在，创建一个围绕它的类并重新定义一些方法：

```python
>>> class MySpam:
        def __init__(self):
            self._spam = Spam()
        def a(self):
            print('MySpam.a')
            self._spam.a()
        def c(self):
            print('MySpam.c')
        def __getattr__(self, name):
            return getattr(self._spam, name)

>>> s = MySpam()
>>> s.a()
MySpam.a
Spam.a
>>> s.b()
Spam.b
>>> s.c()
MySpam.c
>>>
```

仔细注意，结果类看起来与继承非常相似。例如，`a()` 方法的行为类似于 `super()` 调用。`b()` 方法是通过 `__getattr__()` 方法获取的，该方法委托给内部持有的 `Spam` 实例。

**讨论**

`__getattr__()` 方法通常在用作其他对象包装器的类上定义。然而，你必须意识到，以这种方式包装另一个对象的过程通常会引入其他复杂性。例如，如果应用程序的任何其他部分使用 `isinstance()` 函数，包装器对象可能会破坏类型检查。

通过 `__getattr__()` 委托方法也不适用于特殊方法，如 `__getitem__()`、`__enter__()` 等等。如果一个类大量使用此类方法，你将必须在包装器类中提供类似的函数。
