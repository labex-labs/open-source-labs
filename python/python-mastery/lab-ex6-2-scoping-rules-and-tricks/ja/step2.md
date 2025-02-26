# あなたの局所変数を見せてください

まず、次のクラスを定義することで実験してみましょう。

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            print(locals())

>>>
```

次に、これを実行してみましょう。

```python
>>> s = Stock('GOOG', 100, 490.1)
{'self': <__main__.Stock object at 0x100699b00>, 'price': 490.1, 'name': 'GOOG','shares': 100}
>>>
```

局所変数の辞書に `__init__()` に渡されたすべての引数が含まれていることに注目してください。これは興味深いです。次に、次の関数とクラスの定義を定義しましょう。

```python
>>> def _init(locs):
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

>>> class Stock:
        def __init__(self, name, shares, price):
            _init(locals())
```

このコードでは、`_init()` 関数は渡された局所変数の辞書からオブジェクトを自動的に初期化するために使用されます。`help(Stock)` とキーワード引数がうまく機能することがわかります。

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>>
```
