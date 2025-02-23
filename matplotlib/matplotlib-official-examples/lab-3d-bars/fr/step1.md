# Importation des bibliothèques et configuration de la figure

Dans la première étape, nous allons importer les bibliothèques nécessaires et configurer la figure et les axes pour le graphique.

```python
import matplotlib.pyplot as plt
import numpy as np

# configure la figure et les axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
```
