# Import necessary libraries and load synthetic data

We start by importing necessary libraries and loading synthetic data. We generate a synthetic random regression dataset and modify the targets by translating all targets such that all entries are non-negative and applying an exponential function to obtain non-linear targets which cannot be fitted using a simple linear model. We then use a logarithmic (np.log1p) and an exponential function (np.expm1) to transform the targets before training a linear regression model and using it for prediction.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Generate synthetic data
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modify the targets
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
