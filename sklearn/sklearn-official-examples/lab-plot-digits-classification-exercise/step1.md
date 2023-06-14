# Load the Digits dataset

We will start by loading the digits dataset using the `load_digits` function from scikit-learn. This function returns two arrays: `X_digits` containing the input data and `y_digits` containing the target labels.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```


