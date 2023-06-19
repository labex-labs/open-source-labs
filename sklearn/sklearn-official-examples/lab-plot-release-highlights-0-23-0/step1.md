# Generalized Linear Models

The scikit-learn 0.23 release added generalized linear models with non-normal loss functions. In this step, we will use the PoissonRegressor to model positive integer counts or relative frequencies.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PoissonRegressor

# create a dataset
n_samples, n_features = 1000, 20
rng = np.random.RandomState(0)
X = rng.randn(n_samples, n_features)
# positive integer target correlated with X[:, 5] with many zeros:
y = rng.poisson(lam=np.exp(X[:, 5]) / 2)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

# create and fit a PoissonRegressor model
glm = PoissonRegressor()
glm.fit(X_train, y_train)

# calculate the model's score
print(glm.score(X_test, y_test))
```


