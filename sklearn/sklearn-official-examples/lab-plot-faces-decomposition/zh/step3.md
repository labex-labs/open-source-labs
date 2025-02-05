# 非负分量 - 非负矩阵分解（NMF）

接下来，我们应用非负矩阵分解（NMF），它将数据矩阵分解为两个非负矩阵，一个包含基向量，另一个包含系数。这会得到数据的基于部分的表示。

```python
# 非负分量 - 非负矩阵分解（NMF）
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # 原始非负数据集
plot_gallery("非负分量 - 非负矩阵分解（NMF）", nmf_estimator.components_[:n_components])
```
