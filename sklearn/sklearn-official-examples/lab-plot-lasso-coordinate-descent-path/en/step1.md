# Load the Dataset

In this step, we will load the diabetes dataset from scikit-learn library and standardize the data.

```python
from sklearn import datasets

# Load the diabetes dataset
X, y = datasets.load_diabetes(return_X_y=True)

# Standardize data
X /= X.std(axis=0)
```
