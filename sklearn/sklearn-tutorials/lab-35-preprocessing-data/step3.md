# Normalization

Normalization is the process of scaling individual samples to have unit norm. It is commonly used when the magnitude of the data is not important and we are only interested in the direction (or angle) of the data. We can use the `Normalizer` from scikit-learn to perform normalization.

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
