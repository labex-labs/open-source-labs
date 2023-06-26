# Split the Dataset

We will split the dataset into training and testing sets using the first 3000 samples for training and the remaining samples for testing.

```python
n_split = 3000
X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]
```
