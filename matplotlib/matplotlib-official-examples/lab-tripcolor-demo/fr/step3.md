# Création d'un graphique en pseudo-couleurs

Maintenant, nous allons créer un graphique en pseudo-couleurs à l'aide de la fonction `tripcolor()`. Nous allons créer deux graphiques en utilisant différentes méthodes d'ombrage.

```python
# Graphique avec ombrage plat
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor de la triangulation de Delaunay, ombrage plat')

# Graphique avec ombrage Gouraud
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
tpc = ax2.tripcolor(triang, z, shading='gouraud')
fig2.colorbar(tpc)
ax2.set_title('tripcolor de la triangulation de Delaunay, ombrage Gouraud')
```
