# PCA を実行する

次に、データセットに対して PCA を実行します。まず、`x`、`y`、および `z` を連結して 3 次元配列 `Y` を形成します。次に、PCA クラスのインスタンスを作成し、データに適合させます。その後、PCA オブジェクトの `components_` 属性を使用して主成分にアクセスできます。

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
