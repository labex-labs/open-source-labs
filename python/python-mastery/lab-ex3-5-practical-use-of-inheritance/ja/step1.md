# 準備

Python におけるクラスの主な使い方の 1 つは、さまざまな方法で拡張/適応できるコードを書くことです。例を挙げると、演習 3.2 では、表を作成する関数 `print_table()` を作成しました。これを使って `portfolio` リストからの出力を作成しました。たとえば：

```python
>>> import stock
>>> import reader
>>> import tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> tableformat.print_table(portfolio, ['name','shares','price'])
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

`print_table()` 関数が CSV、XML、HTML、Excel など、任意の数の出力形式で表を作成できるようにしたいとしましょう。一度にすべての出力形式をサポートするように関数を変更しようとすると、面倒です。これを行うより良い方法は、出力に関連するフォーマットコードをクラスに移動し、異なる出力形式を実装するために継承を使用することです。
