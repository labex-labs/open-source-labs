# Imputation von fehlenden Werten

Fehlende Werte in einem Datensatz können Probleme bei Machine-Learning-Algorithmen verursachen. Wir können die Methoden aus dem `impute`-Modul von scikit-learn verwenden, um fehlende Werte zu behandeln. Hier werden wir den `SimpleImputer` verwenden, um fehlende Werte zu imputieren.

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
