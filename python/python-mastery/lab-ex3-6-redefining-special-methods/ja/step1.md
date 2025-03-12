# `__repr__` を使ったオブジェクト表現の改善

Python では、オブジェクトを文字列として 2 つの異なる方法で表現することができます。これらの表現はそれぞれ異なる目的を持ち、様々なシナリオで役立ちます。

1 つ目は **文字列表現** です。これは `str()` 関数によって作成され、`print()` 関数を使用すると自動的に呼び出されます。文字列表現は人間が読みやすいように設計されており、オブジェクトを理解しやすい形式で提示します。

2 つ目は **コード表現** です。これは `repr()` 関数によって生成されます。コード表現は、オブジェクトを再作成するために必要なコードを示します。コード内でオブジェクトを正確かつ明確に表現する方法を提供することに重点が置かれています。

Python の組み込み `date` クラスを使った具体的な例を見てみましょう。これにより、文字列表現とコード表現の違いを実際に確認することができます。

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

この例では、`print(d)` を使用すると、Python は `date` オブジェクト `d` に対して `str()` 関数を呼び出し、`YYYY-MM-DD` 形式の人間が読みやすい日付が得られます。対話型シェルで単に `d` と入力すると、Python は `repr()` 関数を呼び出し、`date` オブジェクトを再作成するために必要なコードが表示されます。

`repr()` 文字列を明示的に取得する方法はいくつかあります。以下に例を示します。

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

では、この概念を `Stock` クラスに適用しましょう。`__repr__` メソッドを実装することで、このクラスを改善します。この特殊メソッドは、Python がオブジェクトのコード表現を必要とするときに呼び出されます。

これを行うには、エディタで `stock.py` ファイルを開きます。次に、`Stock` クラスに `__repr__` メソッドを追加します。`__repr__` メソッドは、`Stock` オブジェクトを再作成するために必要なコードを示す文字列を返す必要があります。

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

`__repr__` メソッドを追加した後、完成した `Stock` クラスは次のようになります。

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
```

では、修正した `Stock` クラスをテストしましょう。ターミナルで次のコマンドを実行して、Python の対話型シェルを開きます。

```bash
python3
```

対話型シェルが開いたら、次のコマンドを試してみましょう。

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

また、`__repr__` メソッドが株式ポートフォリオでどのように機能するかも確認できます。以下に例を示します。

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

ご覧の通り、`__repr__` メソッドにより、対話型シェルやデバッガで `Stock` オブジェクトを表示する際に、はるかに有益な情報が表示されるようになりました。現在では、各オブジェクトを再作成するために必要なコードが表示されるため、デバッグやオブジェクトの状態の理解に非常に役立ちます。

テストが終了したら、次のコマンドを実行して Python インタープリターを終了できます。

```python
>>> exit()
```
