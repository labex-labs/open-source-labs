# Tranches et incréments

La tranche de base en NumPy étend le concept de tranche de Python aux N dimensions. Elle vous permet de sélectionner une plage d'éléments le long de chaque dimension d'un tableau.

## Tranche de base

La tranche de base se produit lorsque `obj` est un objet de tranche (construit par la notation `start:stop:step` à l'intérieur des crochets), un entier ou un tuple d'objets de tranche et d'entiers.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])  # Sortie : [1, 3, 5]
```

## Indices négatifs

Les indices négatifs peuvent être utilisés pour indexer à partir de la fin du tableau. Par exemple, `-1` fait référence au dernier élément, `-2` fait référence au deuxième élément depuis la fin, etc.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[-2:10])  # Sortie : [8, 9]
print(x[-3:3:-1])  # Sortie : [7, 6, 5, 4]
```

## Valeurs par défaut pour la tranche

Si l'index de début n'est pas spécifié, il prend la valeur par défaut 0 pour les valeurs de pas positives et `-n-1` pour les valeurs de pas négatives. Si l'index de fin n'est pas spécifié, il prend la valeur par défaut `n` pour les valeurs de pas positives et `-n-1` pour les valeurs de pas négatives. Si le pas n'est pas spécifié, il prend la valeur par défaut 1.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[5:])  # Sortie : [5, 6, 7, 8, 9]
```
