# Préparation des coordonnées

Ensuite, nous allons préparer les coordonnées pour notre tracé de voxels. Nous allons créer une grille de points de taille 8x8x8 en utilisant la fonction `indices` de NumPy.

```python
x, y, z = np.indices((8, 8, 8))
```
