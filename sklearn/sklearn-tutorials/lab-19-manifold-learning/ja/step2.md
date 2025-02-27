# 局所的線形埋め込み (Locally Linear Embedding: LLE)

局所的線形埋め込み (LLE) は、もう一つの多様体学習アルゴリズムです。このアルゴリズムは、局所的な近傍内の距離を保つデータの低次元射影を求めます。

```python
from sklearn.manifold import LocallyLinearEmbedding

# LLEアルゴリズムのインスタンスを作成
lle = LocallyLinearEmbedding(n_components=2)

# アルゴリズムをデータに適合させ、データを低次元空間に変換
X_transformed = lle.fit_transform(X)
```
