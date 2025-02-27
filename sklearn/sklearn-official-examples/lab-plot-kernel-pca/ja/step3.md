# PCA を使ってデータセットを射影する

PCA は、データセットの元の変動の大部分を保つ新しい空間にデータセットを射影するために使用されます。

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
