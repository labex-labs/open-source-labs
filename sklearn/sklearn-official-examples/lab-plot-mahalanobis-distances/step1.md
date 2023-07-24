# Generate Data

First, we generate a dataset of 125 samples and 2 features. Both features are Gaussian distributed with a mean of 0. However, feature 1 has a standard deviation equal to 2 and feature 2 has a standard deviation equal to 1. Next, we replace 25 samples with Gaussian outlier samples where feature 1 has a standard deviation equal to 1 and feature 2 has a standard deviation equal to 7.

```python
import numpy as np

# for consistent results
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# generate Gaussian data of shape (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# add some outliers
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
