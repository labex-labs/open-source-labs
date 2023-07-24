# Generate Sample Data

In this step, we generate sample data using a highly non-Gaussian process, 2 student T with a low number of degrees of freedom.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# Mix data
A = np.array([[1, 1], [0, 2]])  # Mixing matrix

X = np.dot(S, A.T)  # Generate observations
```
