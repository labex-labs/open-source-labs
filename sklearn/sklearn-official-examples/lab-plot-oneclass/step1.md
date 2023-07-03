# Import necessary libraries and generate data

The first step is to import the necessary libraries and generate data. We will use numpy and matplotlib for generating and visualizing data, and scikit-learn for building the one-class SVM model.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Generate train data
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Generate some regular novel observations
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Generate some abnormal novel observations
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
