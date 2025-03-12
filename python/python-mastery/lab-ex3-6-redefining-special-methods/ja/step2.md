# `__eq__` を使ってオブジェクトを比較可能にする

Python では、`==` 演算子を使って 2 つのオブジェクトを比較すると、実際には `__eq__` という特殊メソッドが呼び出されます。デフォルトでは、このメソッドはオブジェクトの同一性を比較します。つまり、オブジェクトが同じメモリアドレスに格納されているかどうかをチェックし、内容を比較するわけではありません。

例を見てみましょう。`Stock` クラスがあり、同じ値を持つ 2 つの `Stock` オブジェクトを作成したとします。そして、`==` 演算子を使ってこれらを比較しようとします。Python インタープリターでは次のように操作できます。

まず、ターミナルで次のコマンドを実行して Python インタープリターを起動します。

```bash
python3
```

次に、Python インタープリターで以下のコードを実行します。

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

ご覧の通り、2 つの `Stock` オブジェクト `a` と `b` の属性（`name`、`shares`、`price`）の値は同じですが、Python はこれらを異なるオブジェクトとみなします。なぜなら、これらは異なるメモリ位置に格納されているからです。

この問題を解決するために、`Stock` クラスに `__eq__` メソッドを実装することができます。このメソッドは、`Stock` クラスのオブジェクトに `==` 演算子が使用されるたびに呼び出されます。

では、再度 `stock.py` ファイルを開きましょう。`Stock` クラスの中に、以下の `__eq__` メソッドを追加します。

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

このメソッドが行うことを分解してみましょう。

1. まず、`isinstance` 関数を使って、`other` オブジェクトが `Stock` クラスのインスタンスであるかどうかをチェックします。これは、`Stock` オブジェクトを他の `Stock` オブジェクトとのみ比較したいからです。
2. `other` が `Stock` オブジェクトである場合、`self` オブジェクトと `other` オブジェクトの属性（`name`、`shares`、`price`）を比較します。
3. 両方のオブジェクトが `Stock` インスタンスであり、それらの属性が同一である場合にのみ `True` を返します。

`__eq__` メソッドを追加した後、完成した `Stock` クラスは次のようになります。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

では、改善した `Stock` クラスをテストしましょう。再度 Python インタープリターを起動します。

```bash
python3
```

次に、Python インタープリターで以下のコードを実行します。

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

素晴らしい！これで、`Stock` オブジェクトはメモリアドレスではなく、内容に基づいて適切に比較できるようになりました。

`__eq__` メソッドの `isinstance` チェックは非常に重要です。これにより、`Stock` オブジェクト同士のみを比較することが保証されます。このチェックがない場合、`Stock` オブジェクトを `Stock` オブジェクトではないものと比較するとエラーが発生する可能性があります。

テストが終了したら、次のコマンドを実行して Python インタープリターを終了できます。

```python
>>> exit()
```
