# 演習7.4：引数の透過

`fileparse.parse_csv()` 関数には、ファイルの区切り文字を変更したり、エラー報告に関するオプションがいくつかあります。おそらくあなたは、上の `read_portfolio()` 関数にこれらのオプションを公開したいでしょう。この変更を行ってください。

    def read_portfolio(filename, **opts):
        '''
        株式ポートフォリオファイルを、name、shares、price のキーを持つ辞書のリストに読み込む。
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

変更を行ったら、いくつかのエラーが含まれるファイルを読み取ってみてください。

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
```

次に、エラーを無視するようにしてみてください。

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```
