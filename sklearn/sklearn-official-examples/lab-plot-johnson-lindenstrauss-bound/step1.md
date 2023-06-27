# Theoretical Bounds

The first step is to explore the theoretical bounds of the Johnson-Lindenstrauss lemma. We will plot the minimum number of dimensions required to guarantee an `eps`-embedding for an increasing number of samples `n_samples`. The distortion introduced by a random projection `p` is asserted by the fact that `p` is defining an `eps`-embedding with good probability as defined by:

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

Where `u` and `v` are any rows taken from a dataset of shape `(n_samples, n_features)` and `p` is a projection by a random Gaussian `N(0, 1)` matrix of shape `(n_components, n_features)` (or a sparse Achlioptas matrix).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# range of admissible distortions
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# range of number of samples (observation) to embed
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, color in zip(eps_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, color=color)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="lower right")
plt.xlabel("Number of observations to eps-embed")
plt.ylabel("Minimum number of dimensions")
plt.title("Johnson-Lindenstrauss bounds:\nn_samples vs n_components")
plt.show()
```
