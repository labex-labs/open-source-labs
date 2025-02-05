# Import libraries and generate data

We will import the necessary libraries, generate random data using the make_regression dataset, and add outliers to the data.

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

# Generate data
n_samples = 1000
n_outliers = 50

X, y, coef = datasets.make_regression(
    n_samples=n_samples,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0,
)

# Add outlier data
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
```
