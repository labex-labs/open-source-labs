# nullable 整数配列の構築

Pandas は、nullable 整数の配列を作成するための`IntegerArray`クラスを提供しています。まずは`IntegerArray`を作成してみましょう。

```python
# 必要なライブラリをインポート
import pandas as pd
import numpy as np

# 欠損値を含む IntegerArray を作成
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# 出力：<IntegerArray>
# [1, 2, <NA>]
# 長さ：3, dtype: Int64
```

配列を作成する際には、データ型を指定するときに文字列エイリアス「Int64」を使用することもできます。すべての NA に似た値は`pandas.NA`に置き換えられます。

```python
# 文字列エイリアス "Int64" を使用して IntegerArray を作成
arr = pd.array([1, 2, np.nan], dtype="Int64")
# 出力：<IntegerArray>
# [1, 2, <NA>]
# 長さ：3, dtype: Int64
```
