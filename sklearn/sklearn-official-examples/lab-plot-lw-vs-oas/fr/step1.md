# Importation des bibliothèques

Tout d'abord, nous devons importer les bibliothèques nécessaires pour ce laboratoire. Nous utiliserons `numpy` pour les calculs numériques, `matplotlib` pour les visualisations et `scikit-learn` pour l'estimation de la covariance.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, cholesky
from sklearn.covariance import LedoitWolf, OAS
```
