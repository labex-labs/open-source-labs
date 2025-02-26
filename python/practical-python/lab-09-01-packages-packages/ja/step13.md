# チャレンジ9.3：トップレベルのスクリプト

`python -m` コマンドを使用すると、ときどき少々奇妙な感じがします。パッケージの不具合を単純に処理するトップレベルのスクリプトを書きたい場合があります。上記のレポートを生成する `print-report.py` というスクリプトを作成します。

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

このスクリプトをトップレベルの `porty-app/` ディレクトリに置きます。その場所で実行できることを確認しましょう。

    $ cd porty-app
    $ python3 print-report.py portfolio.csv prices.csv txt
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

最終的なコードは、現在、次のような構造になっているはずです。

    porty-app/
        portfolio.csv
        prices.csv
        print-report.py
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
