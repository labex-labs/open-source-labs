# 演習 3.15：`main()`関数

`report.py` ファイルに、コマンドラインオプションのリストを受け取り、以前と同じ出力を生成する `main()` 関数を追加します。この関数を使って、次のように対話的に実行できるようにします。

```python
>>> import report
>>> report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
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

`pcost.py` ファイルを変更して、同様の `main()` 関数を持つようにします。

```python
>>> import pcost
>>> pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
Total cost: 44671.15
>>>
```
