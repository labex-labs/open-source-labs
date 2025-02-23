# Personnaliser le graphique d'flèches

La troisième étape consiste à personnaliser le graphique d'flèches. Nous pouvons changer la propriété de la flèche à afficher en utilisant le paramètre `display`. Nous pouvons également changer la forme de la flèche en utilisant le paramètre `shape`. Nous pouvons ajuster la largeur et l'écartement des flèches en utilisant respectivement les paramètres `max_arrow_width` et `arrow_sep`. Nous pouvons changer la transparence des flèches en utilisant le paramètre `alpha`. Nous pouvons également changer la couleur de l'étiquette en utilisant le paramètre `labelcolor`.

```python
# Tracé du graphique d'flèches avec des personnalisations
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
