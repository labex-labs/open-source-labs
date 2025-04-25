# 绘制决策面

在这一步中，我们将在鸢尾花数据集上绘制已定义模型的决策面。

```python
plot_idx = 1

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # 我们只取两个相应的特征
        X = iris.data[:, pair]
        y = iris.target

        # 打乱顺序
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # 标准化
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X = (X - mean) / std

        # 训练
        model.fit(X, y)

        scores = model.score(X, y)
        # 通过使用 str() 并切片去除字符串中无用的部分，为每列和控制台创建一个标题
        model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

        model_details = model_title
        if hasattr(model, "estimators_"):
            model_details += " with {} estimators".format(len(model.estimators_))
        print(model_details + " with features", pair, "has a score of", scores)

        plt.subplot(3, 4, plot_idx)
        if plot_idx <= len(models):
            # 在每列顶部添加一个标题
            plt.title(model_title, fontsize=9)

        # 现在使用精细网格作为填充等高线图的输入来绘制决策边界
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        # 绘制单个决策树分类器，或者对分类器集成的决策面进行 alpha 混合
        if isinstance(model, DecisionTreeClassifier):
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)
        else:
            # 根据正在使用的估计器数量选择 alpha 混合级别
            # （注意，如果 AdaBoost 早期就达到了足够好的拟合，它可以使用比其最大值更少的估计器）
            estimator_alpha = 1.0 / len(model.estimators_)
            for tree in model.estimators_:
                Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

        # 构建一个更粗糙的网格来绘制一组集成分类，以展示它们与我们在决策面中看到的有何不同。这些点是均匀分布的，没有黑色轮廓
        xx_coarser, yy_coarser = np.meshgrid(
            np.arange(x_min, x_max, plot_step_coarser),
            np.arange(y_min, y_max, plot_step_coarser),
        )
        Z_points_coarser = model.predict(
            np.c_[xx_coarser.ravel(), yy_coarser.ravel()]
        ).reshape(xx_coarser.shape)
        cs_points = plt.scatter(
            xx_coarser,
            yy_coarser,
            s=15,
            c=Z_points_coarser,
            cmap=cmap,
            edgecolors="none",
        )

        # 绘制训练点，这些点聚集在一起并有黑色轮廓
        plt.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=ListedColormap(["r", "y", "b"]),
            edgecolor="k",
            s=20,
        )
        plot_idx += 1  # 按顺序转到下一个图

plt.suptitle("鸢尾花数据集特征子集上的分类器", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
```
