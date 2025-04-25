# 局所的線形埋め込み

局所的線形埋め込み（Locally Linear Embedding：LLE）は、グローバルに比較されて最適な非線形埋め込みを見つけるための一連の局所的主成分分析です。ここでは、LLE の 4 つの異なる方法、つまり、標準的な方法、局所接空間整列、ヘッシアン固有写像、および修正された局所的線形埋め込みを使用します。

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
