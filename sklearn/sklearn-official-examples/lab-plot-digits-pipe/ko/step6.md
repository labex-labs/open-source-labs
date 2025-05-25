# PCA 스펙트럼 플롯

각 주성분의 설명된 분산 비율을 시각화하기 위해 PCA 스펙트럼을 플롯합니다.

```python
pca.fit(X_digits)

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True, figsize=(6, 6))
ax0.plot(
    np.arange(1, pca.n_components_ + 1), pca.explained_variance_ratio_, "+", linewidth=2
)
ax0.set_ylabel("PCA 설명된 분산 비율")

ax0.axvline(
    search.best_estimator_.named_steps["pca"].n_components,
    linestyle=":",
    label="선택된 n_components",
)
ax0.legend(prop=dict(size=12))
```
