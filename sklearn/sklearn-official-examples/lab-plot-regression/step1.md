# Generate Sample Data

We first generate sample data to use for our regression problem. We create an array of 40 data points with 1 feature, and then create a target array by applying the sine function to the data. We also add some noise to every 5th data point.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 1 * (0.5 - np.random.rand(8))
```


