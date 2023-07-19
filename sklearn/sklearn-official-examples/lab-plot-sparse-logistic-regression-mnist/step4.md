# Train the Model

We will train the model using logistic regression with L1 penalty and SAGA algorithm. We will set the value of `C` to 50.0 divided by the number of training samples.

```python
# Turn up tolerance for faster convergence
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
