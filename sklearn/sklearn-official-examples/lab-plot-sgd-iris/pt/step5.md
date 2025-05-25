# Plotar Classificadores Um-Contra-Todos

Agora, plotaremos os três classificadores um-contra-todos (OVA) na superfície de decisão. Usaremos os atributos `coef_` e `intercept_` do modelo treinado para plotar os hiperplanos correspondentes aos classificadores OVA.

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
