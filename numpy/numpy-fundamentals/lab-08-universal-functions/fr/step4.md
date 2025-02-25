# Diffusion

La diffusion est une fonction puissante des ufuncs qui permet d'effectuer des opérations sur des tableaux de formes différentes. Les règles de diffusion déterminent la manière dont les tableaux de formes différentes sont traités pendant les opérations. Voyons un exemple.

```python
import numpy as np

# Créez deux tableaux
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])

# Multipliez les tableaux
result = arr1 * arr2

# Affichez le résultat
print(result)
```

Sortie :

```
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```
