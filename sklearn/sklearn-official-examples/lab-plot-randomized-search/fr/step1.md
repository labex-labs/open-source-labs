# Importez les bibliothèques nécessaires et chargez les données

Nous commencerons par importer les bibliothèques nécessaires et charger l'ensemble de données des chiffres à partir de scikit-learn.

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# chargez l'ensemble de données des chiffres
X, y = load_digits(return_X_y=True, n_class=3)
```
