# Aspect de la boîte pour de nombreux sous-graphiques

Il est possible de passer l'aspect de la boîte à un Axe lors de l'initialisation. Le code suivant crée une grille de sous-graphiques 2 x 3 avec tous les Axes carrés.

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```
