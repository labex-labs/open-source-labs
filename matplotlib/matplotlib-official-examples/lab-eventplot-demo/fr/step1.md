# Importation des bibliothèques et définition de la graine aléatoire

Nous allons commencer par importer les bibliothèques nécessaires et définir une graine aléatoire pour la reproductibilité.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)
```
