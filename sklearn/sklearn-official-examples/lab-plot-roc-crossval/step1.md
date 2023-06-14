# Load and prepare data

First, we will load the iris dataset using the Scikit-learn library. The iris dataset contains 3 classes of iris plants, and we will binarize the dataset by dropping one class to create a binary classification problem. We will also add noisy features to make the problem harder.

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y != 2], y[y != 2]
n_samples, n_features = X.shape

# add noisy features
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```


