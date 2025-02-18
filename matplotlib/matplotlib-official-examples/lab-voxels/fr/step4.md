# Définition des couleurs

Nous allons maintenant définir les couleurs de chaque objet dans le tracé de voxels. Pour ce faire, nous allons créer un tableau vide de la même forme que le tableau booléen créé à l'étape 3, puis définir la couleur de chaque objet en fonction de son emplacement.

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
