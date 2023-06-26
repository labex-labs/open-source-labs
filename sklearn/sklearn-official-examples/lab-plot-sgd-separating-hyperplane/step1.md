# Import necessary libraries and generate data

First, we need to import the necessary libraries and generate a dataset that is suitable for classification. In this example, we will generate 50 separable points using the `make_blobs` function from Scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# we create 50 separable points
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```
