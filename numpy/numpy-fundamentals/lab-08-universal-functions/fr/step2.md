# Méthodes des ufuncs

Les ufuncs ont quatre méthodes : reduce, accumulate, reduceat et outer. Ces méthodes sont utiles pour effectuer des opérations sur des tableaux. Jetons un coup d'œil à la méthode reduce.

```python
import numpy as np

# Créez un tableau
arr = np.arange(9).reshape(3, 3)

# Rédigez le tableau le long du premier axe
result = np.add.reduce(arr, 1)

# Affichez le résultat
print(result)
```

Sortie :

```
array([ 3, 12, 21])
```
