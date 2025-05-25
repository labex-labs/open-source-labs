# Plotar Fronteira de Decisão

Neste passo, plotaremos a fronteira de decisão criada no passo anterior. Usaremos os atributos `coef_` e `intercept_` do modelo SVM para plotar a fronteira de decisão.

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
