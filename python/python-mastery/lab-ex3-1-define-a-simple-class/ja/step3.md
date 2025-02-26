# テーブルの出力

手順2で読み込んだデータを表形式にして、見やすい形式のテーブルを作成します。例えば：

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

このコードを、同じ出力を生成するが、さらに表の見出しを追加する `print_portfolio()` 関数に入れます。例えば：

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

## 注:

`stock.py` ファイル内の `print_portfolio()` 関数を完成させます。
