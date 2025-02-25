# Attribution de valeurs à des tableaux indexés

Vous pouvez attribuer des valeurs à des éléments spécifiques ou à des sous-ensembles d'éléments dans un tableau en utilisant l'indexation. La valeur attribuée doit avoir une forme compatible avec le tableau indexé.

```python
x = np.arange(10)
x[2:7] = 1
print(x)  # Sortie : [0, 1, 1, 1, 1, 1, 7, 8, 9]

x = np.arange(10)
x[2:7] = np.arange(5)
print(x)  # Sortie : [0, 1, 0, 1, 2, 3, 7, 8, 9]
```
