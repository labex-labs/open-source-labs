# Tracer la frontière de décision

Dans cette étape, nous allons tracer la frontière de décision créée dans l'étape précédente. Nous utiliserons les attributs `coef_` et `intercept_` du modèle SVM pour tracer la frontière de décision.

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
