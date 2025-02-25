# Création de vues

Les vues peuvent être créées en modifiant certaines métadonnées d'un tableau. Cela crée une nouvelle manière de considérer les données sans les copier. Pour créer une vue, vous pouvez utiliser la méthode `view()` de l'objet `ndarray`.

```python
import numpy as np

# Créez un tableau
x = np.array([1, 2, 3, 4, 5])

# Créez une vue
y = x.view()

# Modifiez la vue
y[0] = 10

# Affichez le tableau d'origine
print(x)  # Sortie : [10, 2, 3, 4, 5]
```

Dans l'exemple ci-dessus, la vue `y` nous permet de modifier le tableau d'origine `x`.
