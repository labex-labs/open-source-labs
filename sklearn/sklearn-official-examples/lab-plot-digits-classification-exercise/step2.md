# Preprocess the data

We will then preprocess the data by scaling the features to a range of [0, 1] using the maximum value of the data. This can be done by dividing the input data by the maximum value of the input data.

```python
X_digits = X_digits / X_digits.max()
```
