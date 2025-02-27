# Générer des données d'échantillonnage

Tout d'abord, nous générons un ensemble de données d'échantillonnage composé de 40 valeurs aléatoires comprises entre 0 et 5. Nous calculons ensuite la fonction sinus de chaque valeur et ajoutons du bruit à chaque 5ème valeur.

```python
import numpy as np

# Générer des données d'échantillonnage
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# ajouter du bruit aux cibles
y[::5] += 3 * (0.5 - np.random.rand(8))
```
