# Effectuer une PCA

Ensuite, nous allons effectuer une PCA sur notre ensemble de données. Nous concaténons d'abord `x`, `y` et `z` pour former un tableau 3D `Y`. Nous créons ensuite une instance de la classe PCA et l'ajustons à nos données. Nous pouvons ensuite accéder aux composantes principales en utilisant l'attribut `components_` de l'objet PCA.

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
