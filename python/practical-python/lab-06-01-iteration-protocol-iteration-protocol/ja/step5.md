# 演習 6.2: 反復処理のサポート

時には、自分自身のオブジェクトの 1 つに反復処理をサポートさせたい場合があります。特に、既存のリストやその他の反復可能オブジェクトをラップしているオブジェクトの場合です。新しいファイル `portfolio.py` で、次のクラスを定義します。

```python
# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

このクラスは、リストの周りのレイヤーとして機能することを意図しており、`total_cost` プロパティなどの追加メソッドがあります。`report.py` の `read_portfolio()` 関数を変更して、次のように `Portfolio` インスタンスを作成します。

    # report.py

...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        株式ポートフォリオファイルを、name、shares、price のキーを持つ辞書のリストに読み込む。
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)

...

`report.py` プログラムを実行してみると、`Portfolio` インスタンスが反復可能でないため、劇的に失敗することがわかります。

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... クラッシュ...
```

`Portfolio` クラスを変更して反復処理をサポートすることでこれを修正します。

```python
class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

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

この変更を行った後、`report.py` プログラムが再び機能するはずです。その際、新しい `Portfolio` オブジェクトを使用するように `pcost.py` プログラムを修正します。次のようになります。

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    ポートフォリオファイルの総コスト (株数 * 価格) を計算する
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

これが機能することを確認するためにテストします。

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
