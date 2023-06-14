# Split Data into Training and Testing Sets

We will split our data into a training set of 400 and a testing set of 200 using scikit-learn's `train_test_split` function.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```


