# Charger le jeu de données de diabète

Nous commençons par charger le jeu de données de diabète à partir de scikit-learn et en sélectionnant seulement une caractéristique du jeu de données.

```python
import numpy as np
from sklearn import datasets

# Charger le jeu de données de diabète
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Utiliser seulement une caractéristique
diabetes_X = diabetes_X[:, np.newaxis, 2]
```
