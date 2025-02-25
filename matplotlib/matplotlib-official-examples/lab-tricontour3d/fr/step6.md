# Créer un tracé de courbe en 3D

Nous allons créer un tracé de courbe en 3D en utilisant la triangulation créée et les coordonnées z. Nous allons également personnaliser l'angle de vue pour faciliter la compréhension du tracé.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
