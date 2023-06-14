# Evaluating the Model

To evaluate the performance of our model, we can use scikit-learn's `accuracy_score` function:

```python
from sklearn.metrics import accuracy_score

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the model
print("Accuracy:", accuracy)
```


