# Training and Testing

We will fit our pipeline on the training data and use it to predict topics for `X_test`. Performance metrics of our pipeline are then printed.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Classification report:\n\n{}".format(classification_report(y_test, y_pred)))
```
