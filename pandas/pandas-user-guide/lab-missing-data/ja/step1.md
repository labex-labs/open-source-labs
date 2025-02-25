# 必要なライブラリをインポートして DataFrame を作成する

まず、必要なライブラリである pandas と NumPy をインポートする必要があります。そして、いくつかの欠損値を持つ DataFrame を作成します。

```python
import pandas as pd
import numpy as np

# 欠損値を持つ DataFrame を作成する
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```
