# Evaluate the Bagging Classifier

Let's evaluate the Bagging Classifier by computing the accuracy score on the test data using the `score` method.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Bagging Classifier Accuracy: {accuracy}")
```
