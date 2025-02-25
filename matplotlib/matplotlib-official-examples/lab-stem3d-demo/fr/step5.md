# Changez l'orientation du tracé

Dans cette étape, nous allons changer l'orientation du tracé à l'aide du paramètre `orientation`. Nous allons définir l'orientation sur `'x'` de sorte que les tiges soient projetées le long de la direction x et que la ligne de base soit dans le plan yz.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
