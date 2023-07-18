# Predict and Measure Accuracy

We predict the class labels for the input data and measure the accuracy of the classifier.

```python
y_pred = clf.predict(X)
print("Accuracy: ", np.mean(y == y_pred))
```
