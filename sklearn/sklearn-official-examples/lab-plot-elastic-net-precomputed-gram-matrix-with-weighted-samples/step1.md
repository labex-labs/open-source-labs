# Loading the Dataset and Creating Sample Weights

We start by loading the dataset and creating some sample weights. We use the `make_regression` function from scikit-learn to generate a random regression dataset with 100,000 samples. Then, we generate a lognormal weight vector and normalize it to sum to the total number of samples.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```


