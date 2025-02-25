# ショートカット関数の使用

`numpy.lib.npyio` モジュールは、`numpy.genfromtxt` から派生したショートカット関数を提供します。これらの関数は異なるデフォルト値を持ち、標準的なNumPy配列またはマスク付き配列を返します。

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
