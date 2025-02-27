# Génération des données

Nous générons deux composants (chaque composant contenant `n_samples`) en échantillonnant aléatoirement la distribution normale standard renvoyée par `numpy.random.randn`. Un composant est conservé sphérique mais déplacé et redimensionné. L'autre est déformé pour avoir une matrice de covariance plus générale.

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # général
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # sphérique

X = np.concatenate([component_1, component_2])
```
