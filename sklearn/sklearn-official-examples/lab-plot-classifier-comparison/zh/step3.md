# 比较分类器

我们将遍历各个分类器，在训练数据上拟合这些分类器，绘制决策边界，并绘制测试数据。我们还将展示测试集上的分类准确率。

```python
# 定义分类器
名称 = [
    "最近邻",
    "线性支持向量机",
    "径向基函数支持向量机",
    "高斯过程",
    "决策树",
    "随机森林",
    "神经网络",
    "AdaBoost",
    "朴素贝叶斯",
    "二次判别分析",
]

分类器 = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1, max_iter=1000),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
]

# 比较分类器
for 名称, 分类器 in zip(名称, 分类器):
    ax = plt.subplot(len(数据集), len(分类器) + 1, i)

    分类器 = make_pipeline(StandardScaler(), 分类器)
    分类器.fit(X_train, y_train)
    得分 = 分类器.score(X_test, y_test)
    DecisionBoundaryDisplay.from_estimator(
        分类器, X, cmap=cm, alpha=0.8, ax=ax, eps=0.5
    )

    ax.scatter(
        X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k"
    )
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())
    if ds_cnt == 0:
        ax.set_title(名称)
    ax.text(
        x_max - 0.3,
        y_min + 0.3,
        ("%.2f" % 得分).lstrip("0"),
        size=15,
        horizontalalignment="right",
    )
    i += 1
```

需注意，文档中“数据集”处原文未给出具体内容，这里保留英文“datasets”以便对照原文理解。
