# 演習 4.5: 拡張可能性の問題

`print_report()` 関数を変更して、平文、HTML、CSV、または XML など、さまざまな異なる出力形式をサポートするようにしたいとします。これを行うために、すべてを行う巨大な関数を書こうとするかもしれません。しかし、そうするとおそらく保守不能な混乱につながります。代わりに、これは継承を使用する完璧な機会です。

始めに、表を作成する際に関係する手順に焦点を当てましょう。表の上部には表の見出しのセットがあります。その後、表データの行が表示されます。これらの手順を取り出して独自のクラスに入れましょう。`tableformat.py` という名前のファイルを作成し、次のクラスを定義します。

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        表の見出しを出力します。
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        表データの 1 行を出力します。
        '''
        raise NotImplementedError()
```

このクラスは何もしませんが、すぐに定義される追加のクラスの一種の設計仕様として機能します。このようなクラスは、時には「抽象基底クラス」と呼ばれます。

`print_report()` 関数を変更して、`TableFormatter` オブジェクトを入力として受け取り、出力を生成するためにそのメソッドを呼び出すようにします。たとえば、次のようになります。

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    (名前，株数，価格，変動) のタプルのリストから、見やすくフォーマットされたテーブルを表示します。
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

`print_report()` に引数を追加したので、`portfolio_report()` 関数も変更する必要があります。それを次のように変更して、`TableFormatter` を作成します。

```python
# report.py

import tableformat

...
def portfolio_report(portfoliofile, pricefile):
    '''
    ポートフォリオと価格データファイルを元に株式レポートを作成します。
    '''
    # データファイルを読み込む
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # レポートデータを作成する
    report = make_report_data(portfolio, prices)

    # それを出力する
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

この新しいコードを実行します。

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... クラッシュ...
```

`NotImplementedError` 例外ですぐにクラッシュするはずです。それはあまり面白くありませんが、まさに私たちが期待したものです。次のパートに進みましょう。
