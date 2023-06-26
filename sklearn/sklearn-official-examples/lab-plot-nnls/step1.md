# Generate Random Data

We will generate some random data to test our algorithm. We will create 200 samples with 50 features and use a true coefficient of 3 for each feature. We will then threshold coefficients to render them non-negative. Lastly, we will add some noise to the samples.

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
