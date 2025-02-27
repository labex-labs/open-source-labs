# Leistung bewerten

Schließlich werden wir die Leistung des Klassifikators (classifier) bewerten, indem wir die Genauigkeit (accuracy) seiner Vorhersagen auf dem Testsatz berechnen.

```python
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
