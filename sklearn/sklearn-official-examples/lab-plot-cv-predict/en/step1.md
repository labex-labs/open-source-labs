# Load and Prepare Data

First, we will load the diabetes dataset and prepare it for modeling. We will use `load_diabetes` function from scikit-learn to load the dataset into two arrays, `X` and `y`.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
