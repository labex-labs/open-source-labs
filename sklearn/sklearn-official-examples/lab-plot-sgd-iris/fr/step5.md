# Tracer les classifieurs un-versus-tous

Nous allons maintenant tracer les trois classifieurs un-versus-tous (OVA) sur la surface de décision. Nous utiliserons les attributs coef* et intercept* du modèle entraîné pour tracer les hyperplans correspondant aux classifieurs OVA.

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
