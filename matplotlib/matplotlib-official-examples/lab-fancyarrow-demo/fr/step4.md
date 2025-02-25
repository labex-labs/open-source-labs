# Tracez les styles de flèche

Tracez chaque style de flèche dans une cellule de la grille, ainsi que ses paramètres par défaut. Utilisez `ax.annotate()` pour ajouter le nom du style de flèche et ses paramètres par défaut à la cellule.

```python
for ax, (stylename, stylecls) in zip(axs[1:, :].T.flat, styles.items()):
    l, = ax.plot(.25,.5, "ok", transform=ax.transAxes)
    ax.annotate(stylename, (.25,.5), (-0.1,.5),
                xycoords="axes fraction", textcoords="axes fraction",
                size="large", color="tab:blue",
                horizontalalignment="center", verticalalignment="center",
                arrowprops=dict(
                    arrowstyle=stylename, connectionstyle="arc3,rad=-0.05",
                    color="k", shrinkA=5, shrinkB=5, patchB=l,
                ),
                bbox=dict(boxstyle="square", fc="w"))
    # wrap at every nth comma (n = 1 or 2, depending on text length)
    s = str(inspect.signature(stylecls))[1:-1]
    n = 2 if s.count(',') > 3 else 1
    ax.text(.35,.5,
            re.sub(', ', lambda m, c=itertools.count(1): m.group()
                   if next(c) % n else '\n', s),
            transform=ax.transAxes,
            horizontalalignment="gauche", verticalalignment="center")
```
