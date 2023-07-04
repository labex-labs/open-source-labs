# Split Data

We will split the dataset into a training set and a test set. The training set will be used to train the SGD classifier, while the test set will be used to evaluate its performance.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
