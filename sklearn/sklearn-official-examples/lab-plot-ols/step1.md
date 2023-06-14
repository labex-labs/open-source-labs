# Load the Diabetes Dataset

We start by loading the diabetes dataset from scikit-learn and only selecting one feature from the dataset.

```python
import numpy as np
from sklearn import datasets

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]
```


