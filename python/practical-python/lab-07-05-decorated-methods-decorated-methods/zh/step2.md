# 静态方法

`@staticmethod` 用于定义所谓的 _静态_ 类方法（源自 C++/Java）。静态方法是类的一部分，但它 _不_ 作用于实例。

```python
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

>>> Foo.bar(2) # x=2
>>>
```

静态方法有时用于为类实现内部支持代码。例如，用于帮助管理已创建实例的代码（内存管理、系统资源、持久性、锁定等）。某些设计模式也会使用它们（此处不讨论）。
