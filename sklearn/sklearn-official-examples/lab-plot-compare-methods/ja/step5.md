# 非線形次元削減のためのスペクトラル埋め込み

この実装では、グラフ・ラプラシアンのスペクトル分解を用いてデータの低次元表現を見つける、ラプラシアン固有写像を使用します。

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
