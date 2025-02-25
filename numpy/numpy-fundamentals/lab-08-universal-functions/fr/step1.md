# Opérations arithmétiques de base

Les ufuncs de base opèrent sur des scalaires, et l'exemple le plus simple est l'opérateur d'addition. Voyons comment nous pouvons utiliser l'opérateur d'addition pour additionner deux tableaux élément par élément.

```python
import numpy as np

# Créez deux tableaux
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# Ajoutez les tableaux élément par élément
result = arr1 + arr2

# Affichez le résultat
print(result)
```

Sortie :

```
array([1, 3, 2, 6])
```
