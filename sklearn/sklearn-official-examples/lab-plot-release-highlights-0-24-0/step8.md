# New Poisson Splitting Criterion for DecisionTreeRegressor

`DecisionTreeRegressor` now supports a new 'poisson' splitting criterion. Setting `criterion="poisson"` might be a good choice if your target is a count or a frequency.

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import numpy as np

# create a random dataset
n_samples, n_features = 1000, 20
rng = np.random.RandomState(0)
X = rng.randn(n_samples, n_features)
y = rng.poisson(lam=np.exp(X[:, 5]) / 2)

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

# create the regressor
regressor = DecisionTreeRegressor(criterion="poisson", random_state=0)

# fit the model
regressor.fit(X_train, y_train)
```
