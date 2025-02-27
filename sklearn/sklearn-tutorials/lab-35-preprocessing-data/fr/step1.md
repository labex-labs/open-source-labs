# Standardization

La standardisation est une étape de prétraitement courante pour de nombreux algorithmes de machine learning. Elle transforme les caractéristiques pour qu'elles aient une moyenne nulle et une variance unitaire. Nous pouvons utiliser le `StandardScaler` de scikit-learn pour effectuer la standardisation.

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
