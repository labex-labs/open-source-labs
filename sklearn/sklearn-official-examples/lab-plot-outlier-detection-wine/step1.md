# Import libraries and load dataset

We will begin by importing the necessary libraries and loading the Wine dataset from scikit-learn. The Wine dataset contains information about different types of wine, including their chemical properties.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load dataset
X1 = load_wine()["data"][:, [1, 2]]  # two clusters
X2 = load_wine()["data"][:, [6, 9]]  # "banana"-shaped
```


