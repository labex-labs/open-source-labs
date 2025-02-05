# 为什么使用 `super()`

重写方法时，始终要使用 `super()`。

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` 会将调用委托给 MRO 中的“下一个类”。

棘手的是，你并不知道这个“下一个类”具体是什么。尤其是在使用多重继承时，你更难确定它是什么。
