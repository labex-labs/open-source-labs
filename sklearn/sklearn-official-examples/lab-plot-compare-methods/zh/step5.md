# 用于非线性降维的谱嵌入

此实现使用拉普拉斯特征映射（Laplacian Eigenmaps），它通过图拉普拉斯矩阵的谱分解来找到数据的低维表示。

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
