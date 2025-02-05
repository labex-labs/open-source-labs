# 绘制一对多分类器

现在我们将在决策面上绘制三个一对多（OVA）分类器。我们将使用训练好的模型的 `coef_` 和 `intercept_` 属性来绘制与 OVA 分类器相对应的超平面。

```python
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
coef = clf.coef_
intercept = clf.intercept_


def plot_hyperplane(c, color):
    def line(x0):
        return (-(x0 * coef[c, 0]) - intercept[c]) / coef[c, 1]

    plt.plot([xmin, xmax], [line(xmin), line(xmax)], ls="--", color=color)


for i, color in zip(clf.classes_, colors):
    plot_hyperplane(i, color)
plt.legend()
plt.show()
```
