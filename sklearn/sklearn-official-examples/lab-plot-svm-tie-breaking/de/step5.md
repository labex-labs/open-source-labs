# Plotten der Entscheidungsgrenze

In diesem Schritt werden wir die in dem vorherigen Schritt erstellte Entscheidungsgrenze plotten. Wir werden die Attribute `coef_` und `intercept_` des SVM-Modells verwenden, um die Entscheidungsgrenze zu plotten.

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
