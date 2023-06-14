# Load the Diabetes Dataset

Next, we will load the diabetes dataset into our program using the `load_diabetes()` function provided by scikit-learn. This function returns the dataset as a tuple of two arrays - one containing the feature data and the other containing the target data. We will assign these arrays to `X` and `y`, respectively.

```python
# Load the diabetes dataset
X, y = load_diabetes(return_X_y=True)
```


