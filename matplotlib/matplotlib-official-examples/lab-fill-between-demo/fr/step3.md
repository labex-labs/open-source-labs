# Remplissage sélectif de régions horizontales

Le paramètre `where` permet de spécifier les plages d'abscisses à remplir. C'est un tableau booléen de même taille que `x`. Seules les plages d'abscisses de séquences consécutives de `True` sont remplies. En conséquence, la plage entre les valeurs `True` et `False` voisines n'est jamais remplie. Il est donc recommandé de définir `interpolate=True` à moins que la distance en abscisses des points de données ne soit suffisamment fine pour que l'effet ci-dessus ne soit pas sensible.

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```
