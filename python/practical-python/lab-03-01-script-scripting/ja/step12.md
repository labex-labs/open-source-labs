# 演習 3.2：プログラム実行用のトップレベル関数の作成

プログラムの最後の部分を取り出して、単一の関数 `portfolio_report(portfolio_filename, prices_filename)` にまとめます。この関数は、次の関数呼び出しが以前と同じようにレポートを作成するように動作するようにします。

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

この最終バージョンでは、プログラムは一連の関数定義の後に、最後に単一の関数呼び出し `portfolio_report()` だけになります（これがプログラムに含まれるすべてのステップを実行します）。

プログラムを単一の関数に変換することで、異なる入力で実行することが簡単になります。たとえば、プログラムを実行した後に対話的に次の文を試してみてください。

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... 出力を見る...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... 出力を見る...
>>>
```
