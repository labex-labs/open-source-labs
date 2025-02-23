# Importation des bibliothèques et configuration des données

Tout d'abord, nous devons importer les bibliothèques nécessaires et configurer certaines données pour le tracé. Dans cet exemple, nous allons tracer trois ondes sinusoïdales avec du bruit aléatoire ajouté.

```python
import matplotlib.pyplot as plt
import numpy as np

# Configuration des données
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```
