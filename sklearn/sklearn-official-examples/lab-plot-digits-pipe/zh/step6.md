# 绘制主成分分析（PCA）频谱

我们将绘制主成分分析（PCA）频谱，以直观显示每个主成分的解释方差比。

```python
pca.fit(X_digits)

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True, figsize=(6, 6))
ax0.plot(
    np.arange(1, pca.n_components_ + 1), pca.explained_variance_ratio_, "+", linewidth=2
)
ax0.set_ylabel("PCA 解释方差比")

ax0.axvline(
    search.best_estimator_.named_steps["pca"].n_components,
    linestyle=":",
    label="所选的 n_components",
)
ax0.legend(prop=dict(size=12))
```
