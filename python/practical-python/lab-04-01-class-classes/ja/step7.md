# 演習 4.1: データ構造としてのオブジェクト

セクション 2 と 3 では、タプルや辞書として表現されたデータを扱いました。たとえば、株式保有は次のようなタプルで表現できます。

```python
s = ('GOOG',100,490.10)
```

または次のような辞書で表現できます。

```python
s = { 'name'   : 'GOOG',
    'shares' : 100,
     'price'  : 490.10
}
```

このようなデータを操作する関数も書けます。たとえば:

```python
def cost(s):
    return s['shares'] * s['price']
```

しかし、プログラムが大きくなるにつれて、もっと組織的な感覚を与えたい場合があります。そこで、データを表現するもう 1 つの方法は、クラスを定義することです。`stock.py` という名前のファイルを作成し、株式の 1 保有を表す `Stock` クラスを定義します。`Stock` のインスタンスに `name`、`shares`、および `price` の属性を持たせます。たとえば:

```python
>>> import stock
>>> a = stock.Stock('GOOG',100,490.10)
>>> a.name
'GOOG'
>>> a.shares
100
>>> a.price
490.1
>>>
```

さらにいくつかの `Stock` オブジェクトを作成して操作してみましょう。たとえば:

```python
>>> b = stock.Stock('AAPL', 50, 122.34)
>>> c = stock.Stock('IBM', 75, 91.75)
>>> b.shares * b.price
6117.0
>>> c.shares * c.price
6881.25
>>> stocks = [a, b, c]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for s in stocks:
     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... 出力を見てください...
>>>
```

ここで強調したいことは、`Stock` クラスがオブジェクトのインスタンスを作成するための工場のように機能することです。基本的には、関数として呼び出すと、新しいオブジェクトを作成してくれます。また、各オブジェクトは個別であり、それぞれ独自のデータを持ち、他の作成されたオブジェクトとは分離されていることも強調する必要があります。

クラスによって定義されるオブジェクトは、辞書に似ていますが、やや異なる構文です。たとえば、`s['name']` や `s['price']` を書く代わりに、今では `s.name` と `s.price` を書きます。
