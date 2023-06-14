# Generate Synthetic Dataset

We generate a synthetic dataset where `X` and `y` are linearly linked. Ten of the features of `X` will be used to generate `y`. The other features are not useful at predicting `y`. In addition, we generate a dataset where `n_samples == n_features`. Such a setting is challenging for an OLS model and leads potentially to arbitrary large weights. Having a prior on the weights and a penalty alleviates the problem. Finally, gaussian noise is added.

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```


