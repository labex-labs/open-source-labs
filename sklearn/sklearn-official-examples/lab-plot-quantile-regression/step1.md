# Dataset Generation

We will generate two synthetic datasets with the same expected value using a linear relationship with a single feature `x`. We will add heteroscedastic normal noise and asymmetric Pareto noise to the datasets.

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# Heteroscedastic Normal noise
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# Asymmetric Pareto noise
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
