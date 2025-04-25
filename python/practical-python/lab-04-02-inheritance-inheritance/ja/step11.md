# 多重継承

クラスの定義で複数のクラスを指定することで、複数のクラスから継承することができます。

```python
class Mother:
...

class Father:
...

class Child(Mother, Father):
...
```

`Child` クラスは両親の特徴を継承します。いくつかかなり厄介な詳細があります。何をしているかを知っている場合を除いてはやめてください。次のセクションでさらに情報を提供しますが、このコースでは多重継承をさらに利用しません。

継承の主な用途は、さまざまな方法で拡張またはカスタマイズすることを目的としたコードの記述です。特にライブラリやフレームワークです。例として、`report.py` プログラムの `print_report()` 関数を考えてみましょう。おそらくこんな感じになっているはずです。

```python
def print_report(reportdata):
    '''
    (名前，株数，価格，変動) のタプルのリストから、見やすくフォーマットされたテーブルを表示します。
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

レポートプログラムを実行すると、次のような出力が得られるはずです。

```python
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
```
