# PCA を実行する

これでデータセットを可視化したので、それに対して PCA を実行しましょう。このために scikit-learn の`PCA()`関数を使います。データセットを 4 次元（4 つの特徴量）から 3 次元に削減したいので、成分数を 3 に設定します。

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
