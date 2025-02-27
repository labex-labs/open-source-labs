# Bewerten des Modells

Schließlich können wir die Genauigkeit unseres Modells bestimmen, indem wir die vorhergesagten Werte mit den wahren Werten vergleichen.

```python
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)
```