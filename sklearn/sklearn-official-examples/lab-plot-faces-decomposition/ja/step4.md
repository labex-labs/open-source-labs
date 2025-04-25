# 独立成分 - FastICA

独立成分分析（ICA）は、多変量信号を最大限独立した加算サブコンポーネントに分離する方法です。私たちは、ICA に対する高速で頑健なアルゴリズムである FastICA を適用します。

```python
# 独立成分 - FastICA
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "Independent components - FastICA", ica_estimator.components_[:n_components]
)
```
