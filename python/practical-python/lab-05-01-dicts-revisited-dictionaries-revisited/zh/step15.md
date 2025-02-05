# “混入（Mixin）”模式

“混入（Mixin）”模式是一种包含代码片段的类。

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

这个类不能单独使用。它通过继承与其他类混合。

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

神奇的是，现在“大声”的功能只实现了一次，就被复用在了两个完全不相关的类中。这种技巧是 Python 中多重继承的主要用途之一。
