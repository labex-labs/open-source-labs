# データ生成

scikit-learn の`make_blobs`関数を使って、異なる分布を持つさまざまなデータセットを生成します。次のコードブロックでは、4 つのデータセットを生成します。

- ガウスブロブの混合
- 異方的に分布するブロブ
- 分散が異なるブロブ
- サイズが不均一なブロブ

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # 異方的なブロブ
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # 分散が異なる
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # サイズが不均一なブロブ
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
