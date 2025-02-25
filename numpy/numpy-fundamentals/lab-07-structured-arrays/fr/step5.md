# Comparaison de tableaux structurés

Si les types de données (dtypes) de deux tableaux structurés sont égaux, nous pouvons les comparer en utilisant l'opérateur d'égalité (`==`). Cela renverra un tableau booléen indiquant quels éléments ont les mêmes valeurs pour tous les champs.

```python
# Compare deux tableaux structurés
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
