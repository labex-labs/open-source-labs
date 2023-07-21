# Sample-weight Support for Lasso and ElasticNet

The Lasso and ElasticNet linear regressors now support sample weights.

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso
import numpy as np

# create a dataset
n_samples, n_features = 1000, 20
rng = np.random.RandomState(0)
X, y = make_regression(n_samples, n_features, random_state=rng)
sample_weight = rng.rand(n_samples)
X_train, X_test, y_train, y_test, sw_train, sw_test = train_test_split(
    X, y, sample_weight, random_state=rng
)

# create and fit a Lasso model with sample weights
reg = Lasso()
reg.fit(X_train, y_train, sample_weight=sw_train)

# calculate the model's score
print(reg.score(X_test, y_test, sw_test))
```
