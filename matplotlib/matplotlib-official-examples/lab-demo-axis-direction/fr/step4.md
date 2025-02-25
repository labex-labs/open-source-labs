# Changement de la direction de l'axe

Maintenant, nous allons créer une boucle pour configurer quatre tracés différents avec l'axe flottant dans chacune des quatre directions cardinaux. Dans la boucle, nous utiliserons `add_floating_axis1()` et `add_floating_axis2()` pour ajouter les axes flottants, et `set_axis_direction()` pour définir la direction de l'axe.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
