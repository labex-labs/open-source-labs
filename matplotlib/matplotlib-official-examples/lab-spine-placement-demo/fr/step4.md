# Créez un graphique à l'aide de la méthode `adjust_spines`

Dans cette étape, nous allons créer un graphique à l'aide de la méthode `adjust_spines` pour démontrer comment ajuster les emplacements des épines.

```python
fig = plt.figure()

x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)

ax = fig.add_subplot(2, 2, 1)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, ['left'])

ax = fig.add_subplot(2, 2, 2)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, [])

ax = fig.add_subplot(2, 2, 3)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, ['left', 'bottom'])

ax = fig.add_subplot(2, 2, 4)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, ['bottom'])

plt.show()
```
