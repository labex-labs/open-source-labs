# 局部线性嵌入

局部线性嵌入（Locally Linear Embedding，LLE）是一系列局部主成分分析，通过全局比较来找到最佳的非线性嵌入。我们将使用四种不同的 LLE 方法，即标准方法、局部切空间对齐、海森特征映射和改进的局部线性嵌入。

```python
params = {
    "n_neighbors": n_neighbors,
    "n_components": n_components,
    "eigen_solver": "auto",
    "random_state": 0,
}

lle_standard = manifold.LocallyLinearEmbedding(method="standard", **params)
S_standard = lle_standard.fit_transform(S_points)

lle_ltsa = manifold.LocallyLinearEmbedding(method="ltsa", **params)
S_ltsa = lle_ltsa.fit_transform(S_points)

lle_hessian = manifold.LocallyLinearEmbedding(method="hessian", **params)
S_hessian = lle_hessian.fit_transform(S_points)

lle_mod = manifold.LocallyLinearEmbedding(method="modified", **params)
S_mod = lle_mod.fit_transform(S_points)
```
