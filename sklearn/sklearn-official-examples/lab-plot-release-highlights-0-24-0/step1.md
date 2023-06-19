# Successive Halving Estimators

Successive Halving is a new state-of-the-art method for exploring the space of hyper-parameters to identify the best combination. In this step, we will explore the `HalvingGridSearchCV` and `HalvingRandomSearchCV` classes that can be used as drop-in replacements for `GridSearchCV` and `RandomizedSearchCV`.

```python
import numpy as np
from scipy.stats import randint
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# create a random dataset
rng = np.random.RandomState(0)
X, y = make_classification(n_samples=700, random_state=rng)

# create a random forest classifier
clf = RandomForestClassifier(n_estimators=10, random_state=rng)

# set the parameter distribution
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 11),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}

# use HalvingRandomSearchCV to find the best parameters
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
rsh.fit(X, y)
print(rsh.best_params_)
```


