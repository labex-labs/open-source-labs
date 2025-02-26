# スクリプトの別の解決策

前述の通り、パッケージ内のスクリプトを実行するには、`-m package.module` を使用する必要があります。

```bash
$ python3 -m porty.pcost portfolio.csv
```

別の方法もあります。新しいトップレベルのスクリプトを書きます。

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

このスクリプトはパッケージの _外側_ にあります。たとえば、ディレクトリ構造を見ると：

    pcost.py       # トップレベルのスクリプト
    porty/         # パッケージディレクトリ
        __init__.py
        pcost.py
      ...
