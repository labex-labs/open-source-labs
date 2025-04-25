# 独立分量 - 快速独立成分分析（FastICA）

独立成分分析（ICA）是一种将多变量信号分离为相互独立的加性子成分的方法。我们应用快速独立成分分析（FastICA），它是一种用于 ICA 的快速且稳健的算法。

```python
# 独立分量 - 快速独立成分分析（FastICA）
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "独立分量 - 快速独立成分分析（FastICA）", ica_estimator.components_[:n_components]
)
```
