# 問題：インポート

同じパッケージ内のファイル間でのインポートでは、_インポートにパッケージ名を含める必要があります_。構造を覚えておいてください。

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

修正されたインポートの例。

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

すべてのインポートは _絶対的_ であり、相対的ではありません。

```python
import fileparse    # エラーになります。fileparseが見つかりません

...
```
