# 距離メトリック

距離メトリックは、2 つのオブジェクト間の非類似性を測定する関数です。これらのメトリックは、非負性、対称性、および三角不等式などの特定の条件を満たします。

一般的な距離メトリックには、ユークリッド距離、マンハッタン距離、およびミンコフスキー距離があります。

`pairwise_distances` 関数を使って、2 つのサンプルセット間のペアワイズ距離を計算してみましょう：

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise distances between X and Y
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

出力：

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
