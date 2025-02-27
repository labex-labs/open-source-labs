# Standardisierung

Die Standardisierung ist ein üblicher Vorverarbeitungsschritt für viele Machine-Learning-Algorithmen. Sie transformiert die Merkmale, sodass sie einen Mittelwert von Null und eine Varianz von Eins haben. Wir können den `StandardScaler` aus scikit-learn verwenden, um die Standardisierung durchzuführen.

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
