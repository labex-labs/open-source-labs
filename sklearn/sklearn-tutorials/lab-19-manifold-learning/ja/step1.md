# Isomap

Isomap アルゴリズムは、多様体学習の初期のアプローチの 1 つです。すべての点間の測地距離を維持する低次元埋め込みを求めます。

```python
from sklearn.manifold import Isomap

# Isomap アルゴリズムのインスタンスを作成
isomap = Isomap(n_components=2)

# アルゴリズムをデータに適合させ、データを低次元空間に変換
X_transformed = isomap.fit_transform(X)
```
