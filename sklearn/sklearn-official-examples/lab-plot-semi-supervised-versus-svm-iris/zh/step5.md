# 可视化决策边界

我们将创建一个覆盖输入特征空间的点的网格，并使用每个分类器预测网格中点的标签。然后，我们将绘制决策边界和标记的数据点。

```python
# 创建一个用于绘制的网格
h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# 为标签定义一个颜色映射
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}

# 设置分类器
classifiers = (ls30, st30, ls50, st50, ls100, rbf_svc)

# 为每个分类器绘制决策边界和标记的数据点
for i, (clf, y_train, title) in enumerate(classifiers):
    # 绘制决策边界
    plt.subplot(3, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 将结果放入颜色图中
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis("off")

    # 绘制标记的数据点
    colors = [color_map[y] for y in y_train]
    plt.scatter(X[:, 0], X[:, 1], c=colors, edgecolors="black")

    plt.title(title)

plt.suptitle("未标记的点为白色", y=0.1)
plt.show()
```
