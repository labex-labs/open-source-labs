# 演習 7.7：繰り返しを避けるためのクロージャの使用

クロージャのより強力な機能の 1 つは、繰り返しコードを生成する際の使用です。演習 5.7 に戻ると、型チェック付きのプロパティを定義するコードを思い出してください。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
  ...
```

そのコードを何度も何度も繰り返して入力する代わりに、クロージャを使って自動的に生成することができます。

`typedproperty.py` というファイルを作成し、次のコードを入れます。

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

次に、このようなクラスを定義して試してみましょう。

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

インスタンスを作成し、型チェックが機能することを確認してみましょう。

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... 型エラーが発生するはずです...
>>>
```
