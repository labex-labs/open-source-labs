# Vorhersagen treffen

Sobald der Klassifizierer trainiert ist, können wir ihn verwenden, um Vorhersagen für die Testdaten zu treffen.

```python
# Make predictions on the test data
y_pred = clf.predict(X_test)

# Print the predicted values
print("Predicted values:", y_pred)
```