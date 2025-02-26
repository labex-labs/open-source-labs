# 演習4.6: 継承を使って異なる出力を生成する

(a) で定義した `TableFormatter` クラスは、継承を通じて拡張することを目的としています。実際、それが全体のアイデアです。例として、次のように `TextTableFormatter` クラスを定義します。

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    平文形式で表を出力します
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

`portfolio_report()` 関数を次のように変更して試してみましょう。

```python
# report.py
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
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
```

これは以前と同じ出力を生成するはずです。

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

しかし、出力を別のものに変更しましょう。CSV形式で出力を生成する新しいクラス `CSVTableFormatter` を定義します。

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    ポートフォリオデータをCSV形式で出力します。
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

メインプログラムを次のように変更します。

```python
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
    formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)
```

これで、次のようなCSV出力が表示されるはずです。

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
```

同じ考え方を使って、次の出力を持つ表を生成する `HTMLTableFormatter` クラスを定義します。

    <tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
    <tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
    <tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
    <tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
    <tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
    <tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
    <tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
    <tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>

メインプログラムを変更して、`CSVTableFormatter` オブジェクトの代わりに `HTMLTableFormatter` オブジェクトを作成することでコードをテストします。
