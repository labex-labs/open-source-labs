# Load and Prepare Data

We begin by importing the necessary libraries and loading the iris dataset. We will then shuffle the data and standardize it to be used for training.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# load iris dataset
iris = datasets.load_iris()

# take the first two features
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# shuffle the data
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# standardize the data
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```
