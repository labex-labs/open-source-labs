# Замена пропущенных значений

Пропущенные значения в наборе данных могут вызывать проблемы при использовании алгоритмов машинного обучения. Мы можем использовать методы, предоставляемые в модуле `impute` библиотеки scikit-learn, для обработки пропущенных значений. Здесь мы будем использовать `SimpleImputer` для замены пропущенных значений.

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
