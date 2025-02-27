# Skalierung

Das Skalieren von Merkmalen in einen bestimmten Bereich ist eine weitere übliche Vorverarbeitungstechnik. Sie ist nützlich, wenn Merkmale unterschiedliche Skalen haben und wir sie alle in einen ähnlichen Bereich bringen möchten. Der `MinMaxScaler` und der `MaxAbsScaler` können verwendet werden, um die Skalierung durchzuführen.

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
