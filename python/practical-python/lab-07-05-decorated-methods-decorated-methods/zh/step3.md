# 类方法

`@classmethod` 用于定义类方法。类方法是一种将 _类_ 对象作为第一个参数而非实例接收的方法。

```python
class Foo:
    def bar(self):
        print(self)
    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # 实例 `f`
>>> Foo.spam()
<class '__main__.Foo'>              # 类 `Foo`
>>>
```

类方法最常被用作定义备用构造函数的工具。

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        # 注意类是如何作为参数传递的
        tm = time.localtime()
        # 并用于创建一个新实例
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

类方法解决了一些与继承等特性相关的棘手问题。

```python
class Date:
  ...
    @classmethod
    def today(cls):
        # 获取正确的类（例如 `NewDate`）
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
  ...

d = NewDate.today()
```
