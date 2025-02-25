# Création d'un sous-graphique

Nous allons créer un sous-graphique pour afficher les segments de ligne colorés. Nous utiliserons la fonction `subplots` de `matplotlib.pyplot` pour créer une grille de sous-graphiques 2x1, et les paramètres `sharex` et `sharey` pour partager les axes x et y entre les sous-graphiques.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
