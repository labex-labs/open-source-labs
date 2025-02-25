# Configurez la figure

Configurez la figure à l'aide de `plt.figure()` et `add_gridspec()`. La figure aura une grille de 2 colonnes et n lignes, où n est le nombre de styles de flèche. Chaque cellule de la grille contiendra un style de flèche et ses paramètres par défaut.

```python
ncol = 2
nrow = (len(styles) + 1) // ncol
axs = (plt.figure(figsize=(4 * ncol, 1 + nrow))
     .add_gridspec(1 + nrow, ncol,
                    wspace=.7, left=.1, right=.9, bottom=0, top=1).subplots())
for ax in axs.flat:
    ax.set_axis_off()
for ax in axs[0, :]:
    ax.text(0,.5, "arrowstyle",
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="center", verticalalignment="center")
    ax.text(.35,.5, "paramètres par défaut",
            transform=ax.transAxes,
            horizontalalignment="gauche", verticalalignment="center")
```
