# Importez les bibliothèques et le jeu de données nécessaires

Tout d'abord, importons les bibliothèques nécessaires et chargeons un jeu de données d'échantillonnage que nous utiliserons pour le biclustering.

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Chargez les données d'échantillonnage
data = np.arange(100).reshape(10, 10)
```
