# Créer un graphique avec des patches hachurées

Vous pouvez également utiliser des hachures avec des patches dans votre graphique. Dans ce cas, nous allons utiliser la fonction `fill_between` pour créer une patch hachurée.

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
