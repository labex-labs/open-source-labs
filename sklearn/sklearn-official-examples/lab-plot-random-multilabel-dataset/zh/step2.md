# 定义绘图函数

接下来，我们定义一个函数 `plot_2d`，用于绘制随机生成的多标签数据集。它接受三个参数 `n_labels`、`n_classes` 和 `length`。

```python
def plot_2d(ax, n_labels=1, n_classes=3, length=50):
    X, Y, p_c, p_w_c = make_ml_clf(
        n_samples=150,
        n_features=2,
        n_classes=n_classes,
        n_labels=n_labels,
        length=length,
        allow_unlabeled=False,
        return_distributions=True,
        random_state=RANDOM_SEED,
    )

    ax.scatter(
        X[:, 0], X[:, 1], color=COLORS.take((Y * [1, 2, 4]).sum(axis=1)), marker="."
    )
    ax.scatter(
        p_w_c[0] * length,
        p_w_c[1] * length,
        marker="*",
        linewidth=0.5,
        edgecolor="black",
        s=20 + 1500 * p_c**2,
        color=COLORS.take([1, 2, 4]),
    )
    ax.set_xlabel("Feature 0 count")
    return p_c, p_w_c
```

此函数使用 `make_multilabel_classification` 函数并传入指定参数来生成数据集。然后，它使用 Matplotlib 库的 `scatter` 函数绘制数据集。该函数返回类别概率和特征概率。
