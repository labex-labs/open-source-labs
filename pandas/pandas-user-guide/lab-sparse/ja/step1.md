# 疎配列の作成

まず、疎配列を作成します。これは、疎な値の配列を効率的に格納するための pandas のデータ構造です。疎な値とは、大部分の値と同じであるため格納されない、冗長と考えられる値のことです。

```python
# 必要なライブラリをインポート
import pandas as pd
import numpy as np

# ランダムな値を持つ numpy 配列を作成
arr = np.random.randn(10)

# いくつかの値を NaN に設定
arr[2:-2] = np.nan

# pandas を使って疎配列を作成
ts = pd.Series(pd.arrays.SparseArray(arr))

# 疎配列を出力
print(ts)
```
