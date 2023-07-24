# Generating Polynomial Features

Sometimes it is beneficial to add complexity to a model by considering nonlinear features of the input data. We can use the `PolynomialFeatures` from scikit-learn to generate polynomial features.

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Create a sample dataset
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# Initialize the PolynomialFeatures
poly = PolynomialFeatures(2)

# Fit and transform the training data
X_poly = poly.fit_transform(X)

# Print the transformed data
print(X_poly)
```
