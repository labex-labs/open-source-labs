# lambda の使用

- lambda は非常に制限されています。
- 1 つの式のみが許可されます。
- `if`、`while` などの文はありません。
- 最も一般的な使い方は、`sort()` のような関数との組み合わせです。

いくつかの株式ポートフォリオデータを読み取り、リストに変換します：

```python
>>> import report
>>> portfolio = list(report.read_portfolio('portfolio.csv'))
>>> for s in portfolio:
        print(s)

Stock('AA', 100, 32.2)
Stock('IBM', 50, 91.1)
Stock('CAT', 150, 83.44)
Stock('MSFT', 200, 51.23)
Stock('GE', 95, 40.37)
Stock('MSFT', 50, 65.1)
Stock('IBM', 100, 70.44)
>>>
```
