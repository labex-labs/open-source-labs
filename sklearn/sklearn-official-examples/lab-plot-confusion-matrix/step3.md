# Split Data

We will split the dataset into a training set and a test set. The training set will be used to train the model, and the test set will be used to evaluate the model's performance.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
