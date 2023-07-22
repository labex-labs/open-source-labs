# Imputation of Missing Values

Missing values in a dataset can cause issues with machine learning algorithms. We can use the methods provided in scikit-learn's `impute` module to handle missing values. Here, we will use the `SimpleImputer` to impute missing values.

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
