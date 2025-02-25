# Importation des bibliothèques et génération de données

Nous allons tout d'abord importer les bibliothèques nécessaires et générer des données pour le tracé.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

# Générer des données
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
```
