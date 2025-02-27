# Tracez les courbes d'apprentissage pour chaque ensemble de données

Enfin, nous pouvons tracer les courbes d'apprentissage pour chaque ensemble de données en utilisant la fonction plot_on_dataset. Nous créerons un graphique 2x2 et tracerons chaque ensemble de données sur un axe séparé.

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```
