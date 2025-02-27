# サンプルデータの生成

`make_checkerboard`関数を使ってサンプルデータを生成します。`shape=(300, 300)`の各ピクセルは、その色で一様分布からの値を表します。ノイズは正規分布から追加され、`noise`に選択された値は標準偏差です。

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
_ = plt.show()
```
