# クラスの作成

以前の実験で思い出してください。こんな感じのシンプルなクラス `Stock` を定義しました。

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares
```

ここで行うことは、手動でクラスを作成することです。まずは、通常のPython関数としてメソッドを定義しましょう。

```python
>>> def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

>>> def cost(self):
        return self.shares*self.price

>>> def sell(self,nshares):
        self.shares -= nshares

>>>
```

次に、メソッド辞書を作成します。

```python
>>> methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell }

>>>
```

最後に、`Stock` クラスオブジェクトを作成します。

```python
>>> Stock = type('Stock',(object,),methods)
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>> s.sell(25)
>>> s.shares
75
>>>
```

おめでとうございます。これでクラスを作成しました。クラスは、実は名前と、基底クラスのタプル、そしてクラスのすべての内容を保持する辞書に他なりません。`type()` は、これら3つの部分を提供すればクラスを作成するコンストラクタです。
