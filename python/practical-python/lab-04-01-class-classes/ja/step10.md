# 演習 4.4: クラスの使用

`report.py` プログラムの `read_portfolio()` 関数を変更して、演習 4.3 で示したように、ポートフォリオを `Stock` インスタンスのリストに読み込みます。その後、`report.py` と `pcost.py` のすべてのコードを修正して、辞書ではなく `Stock` インスタンスと動作するようにします。

ヒント：コードを大きく変更する必要はありません。主に辞書アクセスを `s['shares']` から `s.shares` のように変更するだけです。

以前と同じように関数を実行できるはずです。

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
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
