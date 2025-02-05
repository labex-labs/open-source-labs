# Split Data

We will split the dataset into a training set and a test set using the `train_test_split` function.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
