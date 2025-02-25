# Détermination du type de sortie

La sortie d'une ufunc n'est pas nécessairement un ndarray si tous les arguments d'entrée ne sont pas des ndarrays. Le type de sortie peut être déterminé en fonction des types d'entrée et des règles de moulage de type. Voyons un exemple.

```python
import numpy as np

# Créez un tableau
arr = np.arange(9).reshape(3, 3)

# Effectuez une multiplication et spécifiez le type de sortie
result = np.multiply.reduce(arr, dtype=float)

# Affichez le résultat
print(result)
```

Sortie :

```
array([ 0., 28., 80.])
```
