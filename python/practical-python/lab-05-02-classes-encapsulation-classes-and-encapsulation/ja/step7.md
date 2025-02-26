# プロパティ

前のパターンに代わるアプローチがあります。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

通常の属性アクセスは、今では `@property` と `@shares.setter` の下のゲッターとセッターメソッドをトリガーします。

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # @property をトリガー
50
>>> s.shares = 75    # @shares.setter をトリガー
>>>
```

このパターンでは、ソースコードに変更は必要ありません。新しいセッターは、クラス内での代入時、`__init__()` メソッド内を含めても呼び出されます。

```python
class Stock:
    def __init__(self, name, shares, price):
     ...
        # この代入は下のセッターを呼び出します
        self.shares = shares
     ...

  ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

プロパティとプライベート名の使用の間にはしばしば混乱があります。プロパティは内部的に `_shares` のようなプライベート名を使用しますが、クラスの残りの部分（プロパティではない）は `shares` のような名前を引き続き使用できます。

プロパティは計算されたデータ属性にも便利です。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
  ...
```

これにより、余分な丸括弧を省略でき、実際にはメソッドであることを隠すことができます。

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # インスタンス変数
100
>>> s.cost   # 計算された値
49010.0
>>>
```
