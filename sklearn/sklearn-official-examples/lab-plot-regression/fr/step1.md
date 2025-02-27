# Générer des données d'échantillonnage

Nous commençons par générer des données d'échantillonnage pour notre problème de régression. Nous créons un tableau de 40 points de données avec 1 caractéristique, puis nous créons un tableau cible en appliquant la fonction sinus aux données. Nous ajoutons également du bruit à chaque 5ème point de données.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Ajoutez du bruit aux cibles
y[::5] += 1 * (0.5 - np.random.rand(8))
```
