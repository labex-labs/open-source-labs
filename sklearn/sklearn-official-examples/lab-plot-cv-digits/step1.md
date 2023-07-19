# Load the dataset

First, we need to load the digits dataset from scikit-learn and split it into features and labels.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
