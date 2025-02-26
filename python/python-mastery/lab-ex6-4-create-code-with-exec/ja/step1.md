# exec() を使った実験

文字列で Python コードの断片を定義して実行してみましょう。

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
>>>
```

面白いですが、ランダムなコード断片を実行することは特に役に立ちません。`exec()` のもっと面白い使い方は、関数、メソッド、クラスなどのコードを作成することです。クラス用の `__init__()` 関数を作成する次の例を試してみましょう。

```python
>>> class Stock:
        _fields = ('name','shares', 'price')

>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
        code += f'    self.{name} = {name}\n'
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # 今クラスを試してみましょう
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>>
```

この例では、`__init__()` 関数が直接 `_fields` 変数から作成されます。特殊な `_init()` メソッドやスタックフレームを使った奇妙なハックはありません。
