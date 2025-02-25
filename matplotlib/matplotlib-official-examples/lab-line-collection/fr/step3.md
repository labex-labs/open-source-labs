# Création d'une collection de lignes

Maintenant, nous pouvons créer un objet `LineCollection` avec la fonction `LineCollection`. Nous pouvons définir les paramètres `linewidths`, `colors` et `linestyle` pour personnaliser l'apparence des lignes.

```python
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

segs = np.zeros((50, 100, 2))
segs[:, :, 1] = ys
segs[:, :, 0] = x

segs = np.ma.masked_where((segs > 50) & (segs < 60), segs)

line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2),
                               colors=colors, linestyle='solid')
```
