# Importation des bibliothèques et génération de données

Nous commençons par importer les bibliothèques nécessaires et en générer des données factices.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Générer des données factices
np.random.seed(19680801)
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
