# Den Bagging-Klassifizierer bewerten

Lassen Sie uns den Bagging-Klassifizierer bewerten, indem wir die Genauigkeit auf den Testdaten mit der `score`-Methode berechnen.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Genauigkeit des Bagging-Klassifizierers: {accuracy}")
```