# Scaling

Scaling features to a specific range is another common preprocessing technique. It is useful when features have different scales and we want to bring them all to a similar range. The `MinMaxScaler` and `MaxAbsScaler` can be used to perform scaling.

```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the MinMaxScaler
min_max_scaler = MinMaxScaler()

# Fit and transform the training data
X_minmax = min_max_scaler.fit_transform(X)

# Print the transformed data
print(X_minmax)

# Initialize the MaxAbsScaler
max_abs_scaler = MaxAbsScaler()

# Fit and transform the training data
X_maxabs = max_abs_scaler.fit_transform(X)

# Print the transformed data
print(X_maxabs)
```
