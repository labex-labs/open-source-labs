# Créez le graphique

Nous allons utiliser la fonction `contourf` pour créer un graphique de courbes de niveau remplies avec une échelle de couleur logarithmique :

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
