# Création d'une collection d'ellipses

Nous créons une `EllipseCollection` avec les données ci-dessus et spécifions que les unités sont 'x' et les décalages sont `XY`.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
