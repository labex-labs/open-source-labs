# Création des cubes et du lien

Maintenant, nous allons créer les deux cubes et le lien entre eux. Nous allons le faire en définissant trois tableaux booléens qui seront combinés en un seul tableau booléen. Les deux premiers tableaux définissent l'emplacement des cubes, tandis que le troisième tableau définit l'emplacement du lien.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```
