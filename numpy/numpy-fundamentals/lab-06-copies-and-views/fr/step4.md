# Opérations d'indexation

Les opérations d'indexation dans NumPy peuvent créer soit des vues, soit des copies, selon le type d'indexation.

- L'indexation de base crée toujours des vues. Par exemple :

```python
import numpy as np

# Créez un tableau
x = np.arange(10)

# Créez une vue
y = x[1:3]

# Modifiez la vue
y[0] = 10

# Affichez le tableau d'origine
print(x)  # Sortie : [0, 10, 2, 3, 4, 5, 6, 7, 8, 9]
```

Dans l'exemple ci-dessus, la vue `y` reflète les modifications apportées au tableau d'origine `x`.

- L'indexation avancée crée toujours des copies. Par exemple :

```python
import numpy as np

# Créez un tableau
x = np.arange(9).reshape(3, 3)

# Créez une copie
y = x[[1, 2]]

# Modifiez le tableau d'origine
x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]

# Affichez la copie
print(y)  # Sortie : [[3, 4, 5], [6, 7, 8]]
```

Dans l'exemple ci-dessus, la copie `y` reste inchangée après la modification du tableau d'origine `x`.
