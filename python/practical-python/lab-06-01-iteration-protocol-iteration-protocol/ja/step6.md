# 演習6.3: より適切なコンテナの作成

コンテナクラスを作成する場合、反復処理だけでなく他のことも行いたいことがよくあります。`Portfolio` クラスを変更して、次のような他の特殊メソッドを持たせます。

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

この新しいクラスを使っていくつかの実験をしてみましょう。

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> len(portfolio)
7
>>> portfolio[0]
Stock('AA', 100, 32.2)
>>> portfolio[1]
Stock('IBM', 50, 91.1)
>>> portfolio[0:3]
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44)]
>>> 'IBM' in portfolio
True
>>> 'AAPL' in portfolio
False
>>>
```

これに関する重要な観察点は1つです。一般的に、コードがPythonの他の部分が通常どのように機能するかの共通の語彙を使っている場合、そのコードは「Python風」と考えられます。コンテナオブジェクトの場合、反復処理、インデックス付け、含まれるかどうかの判定、その他の種類の演算子をサポートすることは、この重要な部分の1つです。
