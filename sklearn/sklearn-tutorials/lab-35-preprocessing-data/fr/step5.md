# Imputation des valeurs manquantes

Les valeurs manquantes dans un ensemble de données peuvent poser des problèmes pour les algorithmes de machine learning. Nous pouvons utiliser les méthodes fournies dans le module `impute` de scikit-learn pour gérer les valeurs manquantes. Ici, nous utiliserons le `SimpleImputer` pour imputer les valeurs manquantes.

```python
from sklearn.impute import SimpleImputer
import numpy as np

# Create a sample dataset with missing values
X = np.array([[1., 2., np.nan],
              [3., np.nan, 5.],
              [np.nan, 4., 6.]])

# Initialize the SimpleImputer
imputer = SimpleImputer()

# Fit and transform the training data
X_imputed = imputer.fit_transform(X)

# Print the transformed data
print(X_imputed)
```
