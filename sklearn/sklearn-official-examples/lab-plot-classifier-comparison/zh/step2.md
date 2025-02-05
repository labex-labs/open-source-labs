# 准备数据集

我们将使用三个合成数据集：月牙形、圆形和线性可分数据集。我们将对每个数据集进行预处理，将它们拆分为训练集和测试集，然后绘制数据集。

```python
# 准备数据集
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1
)
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
线性可分数据集 = (X, y)

数据集 = [
    make_moons(noise=0.3, random_state=0),
    make_circles(noise=0.2, factor=0.5, random_state=1),
    线性可分数据集,
]

# 绘制数据集
figure = plt.figure(figsize=(27, 9))
i = 1
for ds_cnt, ds in enumerate(数据集):
    X, y = ds
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )

    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

    cm = plt.cm.RdBu
    cm_bright = ListedColormap(["#FF0000", "#0000FF"])
    ax = plt.subplot(len(数据集), len(分类器) + 1, i)
    if ds_cnt == 0:
        ax.set_title("输入数据")
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())
    i += 1
```

需注意，文档中“分类器”处原文未给出具体内容，这里保留英文“classifiers”以便对照原文理解。
