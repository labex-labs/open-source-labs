# Plotten von One-Against-All-Klassifizierern

Wir werden nun die drei One-Versus-All (OVA)-Klassifizierer auf der Entscheidungsfläche darstellen. Wir werden die `coef*`- und `intercept*`-Attribute des trainierten Modells verwenden, um die Hyperebenen zu plotten, die den OVA-Klassifizierern entsprechen.

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
