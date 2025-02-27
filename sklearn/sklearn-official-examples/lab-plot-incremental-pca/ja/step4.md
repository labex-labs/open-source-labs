# PCA を実行する

PCA クラスのインスタンスを初期化し、データに適合させることで、Iris データセットに対して PCA を実行します。

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
