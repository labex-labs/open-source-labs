# Standardization

Standardization is a common preprocessing step for many machine learning algorithms. It transforms features to have zero mean and unit variance. We can use the `StandardScaler` from scikit-learn to perform standardization.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler on the training data
scaler.fit(X)

# Transform the training data
X_scaled = scaler.transform(X)

# Print the transformed data
print(X_scaled)
```
