# Duplication, jonction ou mutation de tableaux existants

Une fois que vous avez créé des tableaux, vous pouvez les dupliquer, les joindre ou les muter pour créer de nouveaux tableaux. Lorsque vous assignez un tableau ou ses éléments à une nouvelle variable, utilisez la fonction `np.copy` pour créer un nouveau tableau au lieu d'une vue sur le tableau d'origine. Voici un exemple :

```python
import numpy as np

# Créez un tableau
a = np.array([1, 2, 3, 4])

# Créez une vue sur les deux premiers éléments du tableau
b = a[:2]

# Modifiez la vue
b += 1

# Affichez le tableau d'origine et la vue modifiée
print('a =', a, '; b =', b)
```

Pour joindre des tableaux, vous pouvez utiliser des fonctions telles que `np.vstack`, `np.hstack` et `np.block`. Voici un exemple de jonction de quatre tableaux 2x2 en un tableau 4x4 à l'aide de `np.block` :

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```
