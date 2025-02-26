# チャレンジ9.2：アプリケーションディレクトリの作成

すべてのコードを「パッケージ」に入れるだけでは、アプリケーションには不十分なことが多いです。時にはサポートファイル、ドキュメント、スクリプト、その他のものが必要です。これらのファイルは、上で作成した `porty/` ディレクトリの外に存在する必要があります。

`porty-app` という新しいディレクトリを作成します。チャレンジ9.1で作成した `porty` ディレクトリをそのディレクトリに移動させます。`portfolio.csv` と `prices.csv` のテストファイルをこのディレクトリにコピーします。さらに、自分に関する情報を含む `README.txt` ファイルを作成します。あなたのコードは現在、次のように整理されるはずです。

    porty-app/
        portfolio.csv
        prices.csv
        README.txt
        porty/
            __init__.py
            fileparse.py
            follow.py
            pcost.py
            portfolio.py
            report.py
            stock.py
            tableformat.py
            ticker.py
            typedproperty.py

コードを実行するには、トップレベルの `porty-app/` ディレクトリで作業していることを確認する必要があります。たとえば、ターミナルから：

```python
$ cd porty-app
$ python3
>>> import porty.report
>>>
```

以前のいくつかのスクリプトをメインプログラムとして実行してみましょう。

```python
$ cd porty-app
$ python3 -m porty.report portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

$
```
