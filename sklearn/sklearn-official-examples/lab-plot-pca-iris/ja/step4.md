# PCAを実行する

これでデータセットを可視化したので、それに対してPCAを実行しましょう。このためにscikit-learnの`PCA()`関数を使います。データセットを4次元（4つの特徴量）から3次元に削減したいので、成分数を3に設定します。

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
