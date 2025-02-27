# Построение границы решения

В этом шаге мы построим границу решения, созданную на предыдущем шаге. Мы будем использовать атрибуты `coef_` и `intercept_` модели SVM для построения границы решения.

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
