# クラス変数と継承

`types`のようなクラス変数は、継承が使用される場合にカスタマイズメカニズムとして時々使用されます。たとえば、`Stock`クラスでは、サブクラスで型を簡単に変更できます。次の例を試してみてください。この例では、`price`属性を`Decimal`インスタンスに変更しています（これは多くの場合、金融計算により適しています）。

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        types = (str, int, Decimal)

>>> row = ['AA', '100', '32.20']
>>> s = DStock.from_row(row)
>>> s.price
Decimal('32.20')
>>> s.cost()
Decimal('3220.0')
>>>
```

**デザインに関する考察**

この実験で取り組んでいる問題は、ファイルから読み取ったデータの変換に関係しています。代わりに、`Stock`クラスの`__init__()`メソッドでこれらの変換を行うということは理にかなっていますか？たとえば：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

このようにすると、次のようにデータの行を変換できます。

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock(*row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>>
```

これは良いことでしょうか、悪いことでしょうか？あなたの考えは何ですか？全体として、これは疑問視できるデザインだと思います。なぜなら、インスタンスの作成とデータの変換という2つの異なることを混ぜ合わせているからです。さらに、`__init__()`内の暗黙的な変換は柔軟性を制限し、ユーザーが注意深く見ていない場合、奇妙なバグを引き起こす可能性があります。
