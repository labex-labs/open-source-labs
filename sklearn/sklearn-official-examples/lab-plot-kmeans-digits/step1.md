# Load the Dataset

We will start by loading the digits dataset using scikit-learn's `load_digits()` function. This function returns the features and labels for the dataset.

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
