# 可视化数据

在这一步中，我们将可视化我们要处理的数据。数据由 100 个随机生成的输入数据点、3 个在数据点中分布不均匀的类别以及 10 个在数据点中均匀分布的“组”组成。

```python
# 生成类别/组数据
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0.1, 0.3, 0.6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

# 生成不均匀的组
group_prior = rng.dirichlet([2] * 10)
groups = np.repeat(np.arange(10), rng.multinomial(100, group_prior))


def visualize_groups(classes, groups, name):
    # 可视化数据集组
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(groups)),
        [0.5] * len(groups),
        c=groups,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.scatter(
        range(len(groups)),
        [3.5] * len(groups),
        c=classes,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.set(
        ylim=[-1, 5],
        yticks=[0.5, 3.5],
        yticklabels=["数据\n组", "数据\n类别"],
        xlabel="样本索引"
    )


visualize_groups(y, groups, "无组")
```
