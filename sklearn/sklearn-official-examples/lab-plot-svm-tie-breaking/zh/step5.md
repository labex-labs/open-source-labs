# 绘制决策边界

在这一步中，我们将绘制上一步中创建的决策边界。我们将使用支持向量机（SVM）模型的 `coef_` 和 `intercept_` 属性来绘制决策边界。

```python
    for coef, intercept, col in zip(svm.coef_, svm.intercept_, classes):
        line2 = -(line * coef[1] + intercept) / coef[0]
        ax.plot(line2, line, "-", c=colors[col[0]])
        ax.plot(line2, line, "--", c=colors[col[1]])
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title)
    ax.set_aspect("equal")
```
