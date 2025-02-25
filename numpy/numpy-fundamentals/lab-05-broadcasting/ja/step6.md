# 実用例 - ベクトル量子化

ブロードキャストが役立つ実用例を見てみましょう。情報理論や分類において使用されるベクトル量子化（VQ）アルゴリズムを考えてみます。VQの基本操作は、与えられた点に最も近い点を一連の点の中から見つけることです。これはブロードキャストを使って行うことができます。以下は例です：

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

この例では、`observation` は分類対象の選手の体重と身長を表し、`codes` は異なるクラスの選手を表します。`codes` から `observation` を引くことで、ブロードキャストを使って `observation` と各コードの間の距離を計算します。その後、最も近いコードのインデックスを見つけるために `argmin` 関数を使用します。
