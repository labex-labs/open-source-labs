# Définir zorder pour les graduations et les lignes de grille

Nous pouvons utiliser la méthode `set_axisbelow()` ou le paramètre `axes.axisbelow` pour définir le `zorder` des graduations et des lignes de grille.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
