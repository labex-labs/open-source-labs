# Moyenne pondérée

Écrivez une fonction `weighted_average(nums, weights)` qui prend deux listes de même longueur : `nums` et `weights`. La fonction devrait renvoyer la moyenne pondérée des nombres dans `nums`, où chaque nombre est multiplié par son poids correspondant dans `weights`. La moyenne pondérée est calculée en divisant la somme des produits de chaque nombre et de son poids par la somme des poids.

```python
def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```
