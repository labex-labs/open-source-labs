# Indexation avancée

L'indexation avancée est déclenchée lorsque l'objet de sélection `obj` est un objet séquence non tuple, un ndarray (de type de données entier ou booléen) ou un tuple avec au moins un objet séquence ou ndarray (de type de données entier ou booléen). Il existe deux types d'indexation avancée : l'indexation entière et l'indexation booléenne.

## Indexation d'un tableau d'entiers

L'indexation d'un tableau d'entiers permet de sélectionner des éléments arbitraires dans le tableau en fonction de leur index N-dimensionnel. Chaque tableau d'entiers représente un certain nombre d'indices dans cette dimension.

```python
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])  # Sortie : [7, 7, 9, 2]
print(x[np.array([3, 3, -3, 8])])  # Sortie : [7, 7, 4, 2]
```

## Indexation d'un tableau booléen

L'indexation d'un tableau booléen permet de sélectionner des éléments de tableau en fonction d'une condition booléenne. Le résultat est un nouveau tableau qui contient uniquement les éléments correspondant aux valeurs `True` du tableau booléen.

```python
x = np.array([1., -1., -2., 3])
x[x < 0] += 20
print(x)  # Sortie : [ 1., 19., 18., 3.]
```
