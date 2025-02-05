# Data Generation

We generate two components (each one containing `n_samples`) by randomly sampling the standard normal distribution as returned by `numpy.random.randn`. One component is kept spherical yet shifted and re-scaled. The other one is deformed to have a more general covariance matrix.

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # general
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # spherical

X = np.concatenate([component_1, component_2])
```
