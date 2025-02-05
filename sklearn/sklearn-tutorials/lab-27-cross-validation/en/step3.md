# Split the dataset into training and test sets

To evaluate the performance of our model, we need to split the dataset into a training set and a test set. We will use the `train_test_split` function from the scikit-learn library to do this.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
