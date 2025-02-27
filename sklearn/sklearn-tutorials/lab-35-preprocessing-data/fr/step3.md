# Normalisation

La normalisation est le processus consistant à mettre à l'échelle les échantillons individuels pour qu'ils aient une norme unitaire. Elle est couramment utilisée lorsque l'amplitude des données n'est pas importante et que l'on n'est intéressé que par la direction (ou l'angle) des données. Nous pouvons utiliser le `Normalizer` de scikit-learn pour effectuer la normalisation.

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the Normalizer
normalizer = Normalizer()

# Fit and transform the training data
X_normalized = normalizer.fit_transform(X)

# Print the transformed data
print(X_normalized)
```
