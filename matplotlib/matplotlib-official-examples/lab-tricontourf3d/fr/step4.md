# Création du tracé

Maintenant, nous allons créer le tracé à l'aide de la fonction `tricontourf()` et personnaliser l'angle de vue.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
