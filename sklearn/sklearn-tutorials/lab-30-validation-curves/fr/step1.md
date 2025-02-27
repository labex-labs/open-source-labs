# Importez les bibliothèques requises et chargez les données

Commencez par importer les bibliothèques nécessaires et charger un ensemble de données. Dans cet exemple, nous utiliserons l'ensemble de données Iris.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```
