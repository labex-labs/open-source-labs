# 全対一（OVA）分類器をプロットする

ここでは、決定面上に3つの全対一（OVA）分類器をプロットします。訓練済みモデルのcoef*およびintercept*属性を使用して、OVA分類器に対応する超平面をプロットします。

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
