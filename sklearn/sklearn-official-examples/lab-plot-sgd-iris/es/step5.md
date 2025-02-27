# Graficar clasificadores One-Against-All

Ahora graficaremos los tres clasificadores one-versus-all (OVA) en la superficie de decisión. Usaremos los atributos coef* e intercept* del modelo entrenado para graficar los hiperplanos correspondientes a los clasificadores OVA.

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
