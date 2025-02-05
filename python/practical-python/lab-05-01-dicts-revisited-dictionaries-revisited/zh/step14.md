# 一种奇特的代码复用方式（涉及多重继承）

考虑两个完全不相关的对象：

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # 与下面的 LoudBike 有代码共性
        return super().noise().upper()
```

以及

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # 与上面的 LoudDog 有代码共性
        return super().noise().upper()
```

在 `LoudDog.noise()` 和 `LoudBike.noise()` 的实现中存在代码共性。实际上，代码是完全相同的。自然地，这样的代码必然会吸引软件工程师的注意。
