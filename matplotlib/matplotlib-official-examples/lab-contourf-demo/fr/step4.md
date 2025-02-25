# Définir la carte de couleurs et les paramètres d'extension

Enfin, nous allons définir la carte de couleurs et les paramètres d'extension. Nous utiliserons la méthode `with_extremes` pour définir les couleurs pour les valeurs en dehors de la plage des niveaux. Nous créerons également quatre sous-graphiques pour montrer les quatre paramètres d'extension possibles : `'neither'`, `'both'`, `'min'` et `'max'`.

```python
# Définir la carte de couleurs et les paramètres d'extension
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# Créer des sous-graphiques avec différents paramètres d'extension
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# Afficher le tracé
plt.show()
```
