# 演習 4.7: 動的なポリモーフィズム

オブジェクト指向プログラミングの主な特徴の 1 つは、オブジェクトをプログラムに挿入すると、既存のコードを変更することなく動作するということです。たとえば、`TableFormatter` オブジェクトを使用することが期待されるプログラムを書いた場合、実際に与える `TableFormatter` の種類に関係なく動作します。この動作は、時には「ポリモーフィズム」と呼ばれます。

1 つの潜在的な問題は、ユーザーが望むフォーマッタを選ぶ方法を考え出すことです。`TextTableFormatter` のようなクラス名を直接使用するのは、多くの場合面倒です。したがって、いくつかの簡略化されたアプローチを検討するかもしれません。たとえば、次のように `if` 文をコードに埋め込みます。

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    ポートフォリオと価格データファイルを元に株式レポートを作成します。
    '''
    # データファイルを読み込む
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # レポートデータを作成する
    report = make_report_data(portfolio, prices)

    # それを出力する
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    print_report(report, formatter)
```

このコードでは、ユーザーが `'txt'` や `'csv'` のような簡略化された名前を指定して形式を選びます。しかし、そのように `portfolio_report()` 関数に大きな `if` 文を入れるのは最善の考えでしょうか。そのコードを他の場所の汎用関数に移す方が良いかもしれません。

`tableformat.py` ファイルに、`'txt'`、`'csv'`、または `'html'` のような出力名を与えると、ユーザーがフォーマッタを作成できる関数 `create_formatter(name)` を追加します。`portfolio_report()` を次のように変更します。

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    ポートフォリオと価格データファイルを元に株式レポートを作成します。
    '''
    # データファイルを読み込む
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # レポートデータを作成する
    report = make_report_data(portfolio, prices)

    # それを出力する
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

異なる形式で関数を呼び出して、それが機能していることを確認してみましょう。
