# Indexation de base

Les tableaux NumPy peuvent être indexés en utilisant la syntaxe standard Python `x[obj]`, où `x` est le tableau et `obj` est la sélection. Il existe différents types d'indexation disponibles selon le type de `obj`.

## Indexation d'un seul élément

L'indexation d'un seul élément fonctionne exactement comme l'indexation pour les autres séquences standard Python. Elle est basée sur 0 et accepte des indices négatifs pour indexer à partir de la fin du tableau.

```python
x = np.arange(10)
print(x[2])  # Sortie : 2
print(x[-2])  # Sortie : 8
```

## Indexation multidimensionnelle

Les tableaux peuvent avoir plusieurs dimensions, et l'indexation fonctionne de la même manière pour chaque dimension. Vous pouvez accéder à des éléments dans un tableau multidimensionnel en séparant l'index de chaque dimension par une virgule.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Sortie : 8
print(x[1, -1])  # Sortie : 9
```

## Indexation de sous-tableau multidimensionnel

Si vous indexez un tableau multidimensionnel avec moins d'indices que de dimensions, vous obtenez un sous-tableau multidimensionnel. Chaque indice spécifié sélectionne le tableau correspondant aux autres dimensions sélectionnées.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Sortie : [0, 1, 2, 3, 4]
```
