# Generate Synthetic Dataset

First, we generate a dataset where the number of samples is lower than the total number of features. This leads to an underdetermined system, i.e., the solution is not unique, and we cannot apply an ordinary least squares by itself. Regularization introduces a penalty term to the objective function, which modifies the optimization problem and can help alleviate the underdetermined nature of the system. We will generate a target `y` that is a linear combination with alternating signs of sinusoidal signals. Only the 10 lowest out of the 100 frequencies in `X` are used to generate `y`, while the rest of the features are not informative. This results in a high dimensional sparse feature space, where some degree of L1-penalization is necessary.

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # sparsify coef
y = np.dot(X, true_coef)

# introduce random phase using numpy.random.random_sample
# add some gaussian noise using numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# split the data into train and test sets using train_test_split from sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
