# Vérifier si un tableau est une vue ou une copie

Vous pouvez utiliser l'attribut `base` de l'objet `ndarray` pour déterminer si un tableau est une vue ou une copie. L'attribut `base` renvoie le tableau d'origine pour une vue et `None` pour une copie. Par exemple :

```python
import numpy as np

# Créez un tableau
x = np.arange(9)

# Créez une vue
y = x.reshape(3, 3)

# Créez une copie
z = y[[2, 1]]

# Vérifiez si y est une vue
print(y.base)  # Sortie : [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Vérifiez si z est une copie
print(z.base is None)  # Sortie : True
```

Dans l'exemple ci-dessus, `y` est une vue et `z` est une copie.
