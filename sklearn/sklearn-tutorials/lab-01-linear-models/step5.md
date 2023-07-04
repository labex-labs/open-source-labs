# Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent (SGD) is a simple yet efficient approach for training linear models. It is particularly useful when the number of samples and features is very large. SGD updates the model parameters using a small subset of the training data at each iteration, which makes it suitable for online learning and out-of-core learning.

Let's fit a logistic regression model using SGD.

```python
clf = linear_model.SGDClassifier(loss="log", max_iter=1000)
clf.fit(X, y)

print(clf.coef_)
```

- We create an instance of `SGDClassifier` with the `loss` parameter set to "log" to perform logistic regression.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the logistic regression model obtained using SGD.
