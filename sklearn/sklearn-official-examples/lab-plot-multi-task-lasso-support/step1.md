# Generate Data

First, we need to generate some sample data that we can use to fit our models. We will use numpy to generate 100 samples, each with 30 features and 40 tasks. We will also randomly select 5 relevant features and create coefficients for them using sine waves with random frequency and phase. Finally, we will add some random noise to the data.

```python
import numpy as np

rng = np.random.RandomState(42)

# Generate some 2D coefficients with sine waves with random frequency and phase
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```


