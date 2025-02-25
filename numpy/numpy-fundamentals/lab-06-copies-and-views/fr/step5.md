# Autres opérations

Il existe d'autres opérations dans NumPy qui peuvent créer des vues ou des copies.

- La fonction `reshape()` crée une vue si possible, ou une copie sinon. Par exemple :

```python
import numpy as np

# Créez un tableau
x = np.ones((2, 3))

# Transposez le tableau
y = x.T

# Essayez de redimensionner le tableau
try:
    y.shape = 6
except AttributeError:
    print("Incompatible shape for in-place modification. Use `.reshape()` to make a copy with the desired shape.")
```

Dans l'exemple ci-dessus, le tableau `y` devient non-contigu après la transposition, donc le redimensionner nécessite une copie.

- La fonction `ravel()` renvoie une vue aplatie contiguë du tableau dès que possible. En revanche, la méthode `flatten()` renvoie toujours une copie aplatie du tableau. Par exemple :

```python
import numpy as np

# Créez un tableau
x = np.arange(9).reshape(3, 3)

# Créez une vue aplatie
y = x.ravel()

# Créez une copie aplatie
z = x.flatten()

# Affichez le tableau d'origine
print(x)  # Sortie : [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

Dans l'exemple ci-dessus, `y` est une vue, tandis que `z` est une copie.
