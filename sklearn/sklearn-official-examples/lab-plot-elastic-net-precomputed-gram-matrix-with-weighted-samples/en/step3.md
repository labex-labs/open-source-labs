# Fitting the Elastic Net

We can now proceed with fitting. We must pass the centered design matrix to `fit` to prevent the elastic net estimator from detecting that it is uncentered and discarding the gram matrix we passed. However, if we pass the scaled design matrix, the preprocessing code will incorrectly rescale it a second time. We also pass the normalized weights to the `sample_weight` parameter of the `fit` function.

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
