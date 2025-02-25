# Importez les bibliothèques nécessaires et configurez les données

Nous allons importer les bibliothèques `math`, `numpy` et `matplotlib.pyplot` et configurer les données pour les graphiques.

```python
import math
import numpy as np
import matplotlib.pyplot as plt

xmax = 10
x = np.linspace(-xmax, xmax, 10000)
cdf_norm = [math.erf(w / np.sqrt(2)) / 2 + 1 / 2 for w in x]
cdf_laplacian = np.where(x < 0, 1 / 2 * np.exp(x), 1 - 1 / 2 * np.exp(-x))
cdf_cauchy = np.arctan(x) / np.pi + 1 / 2
```
