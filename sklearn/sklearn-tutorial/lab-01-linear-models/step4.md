# Logistic Regression

Logistic regression is a classification method that estimates the probabilities of the possible outcomes using a logistic function. It is commonly used for binary classification tasks. Logistic regression can also be extended to handle multi-class classification problems.

Let's fit a logistic regression model.

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- We create an instance of `LogisticRegression` with the `random_state` parameter set to 0.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the logistic regression model.
