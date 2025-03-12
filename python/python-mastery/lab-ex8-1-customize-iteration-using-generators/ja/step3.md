# 反復処理機能を持つクラスの強化

ここでは、`Structure` クラスとそのサブクラスが反復処理をサポートするようになったことを前提に進めます。反復処理は Python の強力な概念で、コレクション内のアイテムを 1 つずつループで処理できます。クラスが反復処理をサポートすると、より柔軟になり、多くの Python の組み込み機能と連携できるようになります。この反復処理のサポートが Python でどのように強力な機能を可能にするかを見ていきましょう。

## 反復処理を利用したシーケンス変換

Python には `list()` や `tuple()` などの組み込み関数があります。これらの関数は、任意の反復可能オブジェクトを入力として受け取ることができるため、非常に便利です。反復可能オブジェクトとは、リスト、タプル、または今回の `Structure` クラスのインスタンスのように、ループで処理できるものです。`Structure` クラスが反復処理をサポートするようになったので、そのインスタンスを簡単にリストやタプルに変換できます。

1. `Stock` インスタンスでこれらの操作を試してみましょう。`Stock` クラスは `Structure` のサブクラスです。ターミナルで以下のコマンドを実行します。

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

このコマンドはまず `Stock` クラスをインポートし、インスタンスを作成し、それを `list()` と `tuple()` 関数を使ってそれぞれリストとタプルに変換します。出力結果には、インスタンスがリストとタプルとして表されたものが表示されます。

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## アンパッキング

Python にはアンパッキングという非常に便利な機能があります。アンパッキングを使うと、反復可能オブジェクトの要素を一度に個別の変数に割り当てることができます。`Stock` インスタンスは反復可能なので、このアンパッキング機能を使うことができます。

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

このコードでは、`Stock` インスタンスを作成し、その要素を `name`、`shares`、`price` の 3 つの変数にアンパッキングします。そして、これらの変数を出力します。出力結果には、これらの変数の値が表示されます。

```
Name: GOOG, Shares: 100, Price: 490.1
```

## 比較機能の追加

クラスが反復処理をサポートすると、比較操作を実装するのが容易になります。比較操作は、2 つのオブジェクトが等しいかどうかをチェックするために使用されます。`Structure` クラスに `__eq__()` メソッドを追加して、インスタンスを比較できるようにしましょう。

1. 再度 `structure.py` ファイルを開きます。`__eq__()` メソッドは、2 つのオブジェクトを `==` 演算子で比較するときに呼び出される Python の特殊メソッドです。`structure.py` ファイルの `Structure` クラスに以下のコードを追加します。

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

このメソッドはまず、`isinstance()` 関数を使って `other` オブジェクトが `self` と同じクラスのインスタンスであるかをチェックします。そして、`self` と `other` を両方ともタプルに変換し、これらのタプルが等しいかどうかをチェックします。

完成した `structure.py` ファイルは次のようになります。

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. `__eq__()` メソッドを追加した後、`structure.py` ファイルを保存します。

3. 比較機能をテストしてみましょう。ターミナルで以下のコマンドを実行します。

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

このコードは 3 つの `Stock` インスタンス `a`、`b`、`c` を作成します。そして、`==` 演算子を使って `a` と `b`、`a` と `c` を比較します。出力結果には、これらの比較結果が表示されます。

```
a == b: True
a == c: False
```

4. すべてが正しく動作していることを確認するために、ユニットテストを実行する必要があります。ユニットテストは、プログラムのさまざまな部分が期待通りに動作しているかをチェックする一連のコードです。ターミナルで以下のコマンドを実行します。

```bash
python3 teststock.py
```

すべてが正しく動作していれば、テストが合格したことを示す出力が表示されます。

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

`__iter__()` と `__eq__()` という 2 つの簡単なメソッドを追加するだけで、`Structure` クラスに Python らしい機能を追加し、使いやすくすることができました。
