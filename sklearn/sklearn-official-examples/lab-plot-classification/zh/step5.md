# 可视化决策边界

我们将遍历两个不同的权重值，即 “uniform” 和 “distance”，并为每个权重值绘制决策边界。我们将使用 `neighbors` 模块中的 `KNeighborsClassifier` 类来执行分类。

```python
n_neighbors = 15

for weights in ["uniform", "distance"]:
    # 创建一个邻居分类器实例并拟合数据
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # 绘制决策边界
    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=cmap_light,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=iris.feature_names[0],
        ylabel=iris.feature_names[1],
        shading="auto",
    )

    # 绘制训练点
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=iris.target_names[y],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "3-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights)
    )

plt.show()
```
