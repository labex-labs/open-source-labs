# 运行具有方差最大化旋转的因子分析

现在，我们将对鸢尾花数据集运行具有方差最大化旋转的因子分析，以揭示数据的潜在结构。我们将把结果与主成分分析（PCA）和未旋转的因子分析进行比较。

```python
# 运行具有方差最大化旋转的因子分析
n_comps = 2

methods = [
    ("PCA", PCA()),
    ("未旋转的因子分析", FactorAnalysis()),
    ("方差最大化因子分析", FactorAnalysis(rotation="varimax")),
]
fig, axes = plt.subplots(ncols=len(methods), figsize=(10, 8), sharey=True)

for ax, (method, fa) in zip(axes, methods):
    fa.set_params(n_components=n_comps)
    fa.fit(X)

    components = fa.components_.T
    print("\n\n %s :\n" % method)
    print(components)

    vmax = np.abs(components).max()
    ax.imshow(components, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
    ax.set_yticks(np.arange(len(feature_names)))
    ax.set_yticklabels(feature_names)
    ax.set_title(str(method))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["成分 1", "成分 2"])
fig.suptitle("因子")
plt.tight_layout()
plt.show()
```
