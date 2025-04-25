# t-分布型確率的近傍埋め込み (t-distributed Stochastic Neighbor Embedding: t-SNE)

t-SNE は、データポイントの親和性を確率に変換する人気のある多様体学習方法です。高次元データの可視化に特に有効です。

```python
from sklearn.manifold import TSNE

# t-SNE アルゴリズムのインスタンスを作成
tsne = TSNE(n_components=2)

# アルゴリズムをデータに適合させ、データを低次元空間に変換
X_transformed = tsne.fit_transform(X)
```
