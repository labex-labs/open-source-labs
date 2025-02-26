# 演習7.8：関数呼び出しの簡略化

上記の例では、ユーザーは `typedproperty('shares', int)` のような呼び出しを入力するのが少々面倒だと感じるかもしれません。特に、それが何度も繰り返される場合です。`typedproperty.py` ファイルに次の定義を追加します。

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

次に、`Stock` クラスを書き換えて、これらの関数を代わりに使用するようにします。

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

ああ、少しはましです。ここでの主な要点は、クロージャと `lambda` はしばしばコードを簡略化し、厄介な繰り返しを排除するために使用できるということです。これは多くの場合、良いことです。
