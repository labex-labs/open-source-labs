# Data

We generate a classification dataset with 2000 samples, 2 features and 3 target classes. We then split the data as follows:

- train: 600 samples (for training the classifier)
- valid: 400 samples (for calibrating predicted probabilities)
- test: 1000 samples

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

X, y = make_blobs(
    n_samples=2000, n_features=2, centers=3, random_state=42, cluster_std=5.0
)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:1000], y[600:1000]
X_train_valid, y_train_valid = X[:1000], y[:1000]
X_test, y_test = X[1000:], y[1000:]
```
