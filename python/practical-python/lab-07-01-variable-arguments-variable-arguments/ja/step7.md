# 演習7.3：インスタンスのリストを作成する

あなたの `report.py` プログラムでは、次のようなコードを使ってインスタンスのリストを作成しました。

```python
def read_portfolio(filename):
    '''
    株式ポートフォリオファイルを、name、shares、price のキーを持つ辞書のリストに読み込む。
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
```

代わりに `Stock(**d)` を使うことで、そのコードを簡略化できます。その変更を行ってください。
