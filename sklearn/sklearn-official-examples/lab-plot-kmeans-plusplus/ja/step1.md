# サンプルデータを生成する

scikit-learnライブラリの`make_blobs`関数を使ってサンプルデータを生成します。この関数は、クラスタリング用の等方性ガウスブロブを生成します。4つの中心を持つ4000個のサンプルを生成します。

```python
# Generate sample data
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
