# Graficar el límite de decisión

En este paso, graficaremos el límite de decisión creado en el paso anterior. Utilizaremos los atributos `coef_` e `intercept_` del modelo de SVM para graficar el límite de decisión.

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
