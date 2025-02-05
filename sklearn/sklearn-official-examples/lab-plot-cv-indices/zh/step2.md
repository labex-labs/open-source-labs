# 可视化交叉验证索引

在这一步中，我们将定义一个函数来可视化每个交叉验证对象的行为。我们将对数据进行4次分割。在每次分割中，我们将可视化选择用于训练集（蓝色）和测试集（红色）的索引。

```python
def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """为交叉验证对象的索引创建一个示例图。"""

    # 为每个交叉验证分割生成训练/测试可视化
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # 用训练/测试组填充索引
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # 可视化结果
        ax.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # 最后绘制数据类别和组
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # 格式化
    yticklabels = list(range(n_splits)) + ["类别", "组"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="样本索引",
        ylabel="交叉验证迭代",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```
