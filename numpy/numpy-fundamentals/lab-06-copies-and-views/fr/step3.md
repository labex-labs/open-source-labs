# Création de copies

Les copies peuvent être créées en dupliquant à la fois le tampon de données et les métadonnées d'un tableau. Pour créer une copie, vous pouvez utiliser la méthode `copy()` de l'objet `ndarray`.

```python
import numpy as np

# Créez un tableau
x = np.array([1, 2, 3, 4, 5])

# Créez une copie
y = x.copy()

# Modifiez la copie
y[0] = 10

# Affichez le tableau d'origine
print(x)  # Sortie : [1, 2, 3, 4, 5]
```

Dans l'exemple ci-dessus, la copie `y` est indépendante du tableau d'origine `x`.
