# 比较交叉验证对象

在这一步中，我们将比较不同的scikit-learn交叉验证对象的交叉验证行为。我们将遍历几个常见的交叉验证对象，可视化每个对象的行为。注意有些对象如何使用组/类别信息，而有些则不使用。

```python
cvs = [
    KFold,
    GroupKFold,
    ShuffleSplit,
    StratifiedKFold,
    StratifiedGroupKFold,
    GroupShuffleSplit,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
]

for cv in cvs:
    this_cv = cv(n_splits=n_splits)
    fig, ax = plt.subplots(figsize=(6, 3))
    plot_cv_indices(this_cv, X, y, groups, ax, n_splits)

    ax.legend(
        [Patch(color=cmap_cv(0.8)), Patch(color=cmap_cv(0.02))],
        ["测试集", "训练集"],
        loc=(1.02, 0.8),
    )
    # 调整图例使其合适
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```
