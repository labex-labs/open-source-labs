# Générer des données

Nous allons commencer par générer les données. Nous utiliserons l'ensemble de données `coins` de scikit-image, qui est une image en niveaux de gris 2D de pièces. Nous allons redimensionner l'image à 20% de sa taille d'origine pour accélérer le traitement.

```python
from skimage.data import coins
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.transform import rescale

orig_coins = coins()

# Redimensionnez-la à 20% de sa taille d'origine pour accélérer le traitement
# Appliquer un filtre gaussien pour le lissage avant le redimensionnement vers le bas
# réduit les artefacts d'aliasing.

smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(
    smoothened_coins,
    0.2,
    mode="reflect",
    anti_aliasing=False,
)

X = np.reshape(rescaled_coins, (-1, 1))
```
