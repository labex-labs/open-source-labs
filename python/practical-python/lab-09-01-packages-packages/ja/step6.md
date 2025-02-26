# 相対インポート

パッケージ名を直接使用する代わりに、`.` を使って現在のパッケージを参照することができます。

```python
from. import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

構文：

```python
from. import modname
```

これにより、パッケージ名を変更することが簡単になります。
