# Evaluate the Model

We will evaluate the MLPClassifier by computing its accuracy on the training and test sets.

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
