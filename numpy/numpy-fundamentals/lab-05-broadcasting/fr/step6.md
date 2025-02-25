# Exemple pratique - Quantification vectorielle

Explorons un exemple pratique où la diffusion (broadcasting) est utile. Considérons l'algorithme de quantification vectorielle (VQ) utilisé en théorie de l'information et en classification. L'opération de base dans la VQ est de trouver le point le plus proche dans un ensemble de points par rapport à un point donné. Cela peut être fait en utilisant la diffusion (broadcasting). Voici un exemple :

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

Dans cet exemple, `observation` représente le poids et la taille d'un athlète à classifier, et `codes` représente différentes classes d'athlètes. En soustrayant `observation` de `codes`, la diffusion (broadcasting) est utilisée pour calculer la distance entre `observation` et chacun des codes. La fonction `argmin` est ensuite utilisée pour trouver l'indice du code le plus proche.
