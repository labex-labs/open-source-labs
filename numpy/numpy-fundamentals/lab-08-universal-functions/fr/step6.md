# Remplacer le comportement des ufuncs

Les classes, y compris les sous-classes ndarray, peuvent remplacer la manière dont les ufuncs agissent sur elles en définissant certaines méthodes spéciales. Cela permet de personnaliser le comportement des ufuncs. Voyons un exemple.

```python
import numpy as np

# Définissez une classe personnalisée
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Méthode d'addition personnalisée appelée")
        return super().__add__(other)

# Créez une instance de la classe personnalisée
arr = MyArray([1, 2, 3])

# Effectuez une addition
result = arr + 1

# Affichez le résultat
print(result)
```

Sortie :

```
Méthode d'addition personnalisée appelée
[2 3 4]
```
