# 名前の修正

ディスクリプタに関する厄介なことの一つは、冗長な名前指定です。たとえば：

```python
class Stock:
  ...
    shares = PositiveInteger('shares')
  ...
```

これを修正できます。トップレベルの `Validator` クラスを変更して、次のような `__set_name__()` メソッドを含めます：

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

次に、`Stock` クラスを次のように書き直してみましょう：

```python
class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

ああ、はるかに良いです。ただし、この名前を設定する機能はPython 3.6の機能です。古いバージョンでは機能しません。
