# Bewertung des Bagging-Klassifikators

Lassen Sie uns den Bagging-Klassifikator bewerten, indem wir die Genauigkeit (Accuracy) auf den Testdaten mit der Methode `score` berechnen.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Bagging Classifier Accuracy: {accuracy}")
```
