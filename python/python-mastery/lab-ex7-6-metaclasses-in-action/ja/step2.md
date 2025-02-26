# 驚嘆の的に見つめる

この新しいファイルで`teststock.py`の単体テストを実行してみてください。そのほとんどは今では合格するはずです。興味があれば、表の書式設定やデータの読み取りに関する以前のコードの一部を使って`Stock`クラスを試してみてください。すべてうまくいくはずです。

```python
>>> from stock import Stock
>>> from reader import read_csv_as_instances
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

再び、完成した`stock.py`ファイルに驚嘆し、コードがどれほどクリーンに見えるかを見てください。ただ、`Structure`ベースクラスの背後で何が起こっているかを考えないでください。
