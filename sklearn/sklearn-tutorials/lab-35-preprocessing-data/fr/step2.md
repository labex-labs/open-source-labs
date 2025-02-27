# Mise à l'échelle

Mettre les caractéristiques à une plage spécifique est une autre technique de prétraitement courante. Elle est utile lorsque les caractéristiques ont des échelles différentes et que l'on veut les ramener toutes à une plage similaire. Le `MinMaxScaler` et le `MaxAbsScaler` peuvent être utilisés pour effectuer la mise à l'échelle.

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
