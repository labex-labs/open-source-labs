# Load the necessary libraries and MNIST dataset

The first step is to load the necessary libraries and dataset. We will be using `pandas`, `numpy`, `matplotlib`, and `scikit-learn` libraries. We will also use the `fetch_openml` function from scikit-learn to load the MNIST dataset.

```python
import time
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import shuffle

# Load the MNIST dataset
def load_mnist(n_samples=None, class_0="0", class_1="8"):
    """Load MNIST, select two classes, shuffle and return only n_samples."""
    # Load data from http://openml.org/d/554
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="pandas")

    # take only two classes for binary classification
    mask = np.logical_or(mnist.target == class_0, mnist.target == class_1)

    X, y = shuffle(mnist.data[mask], mnist.target[mask], random_state=42)
    if n_samples is not None:
        X, y = X[:n_samples], y[:n_samples]
    return X, y

X, y = load_mnist(n_samples=10000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
