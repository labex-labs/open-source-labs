# Moyenne pondérée

## Problème

Écrivez une fonction `weighted_average(nums, weights)` qui prend deux listes de même longueur : `nums` et `weights`. La fonction devrait renvoyer la moyenne pondérée des nombres dans `nums`, où chaque nombre est multiplié par son poids correspondant dans `weights`. La moyenne pondérée est calculée en divisant la somme des produits de chaque nombre et de son poids par la somme des poids.

## Exemple

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1,72727
```

Explication :

```
(1 * 0,6 + 2 * 0,2 + 3 * 0,3) / (0,6 + 0,2 + 0,3) = 1,72727
```
